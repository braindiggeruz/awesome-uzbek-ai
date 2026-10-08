import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_site as site
import check_content
import check_links


class MarkdownTests(unittest.TestCase):
    def test_duplicate_heading_ids(self):
        result = site.convert("# One\n## Same\n## Same\n")
        self.assertIn('id="same"', result)
        self.assertIn('id="same-1"', result)

    def test_uzbek_anchor(self):
        self.assertEqual(site.slugify("O‘zbek tili (AI)"), "ozbek-tili-ai")
        self.assertEqual(site.slugify("Кирилл ёзуви"), "кирилл-ёзуви")

    def test_badge_removed_from_heading(self):
        result = site.convert("# Awesome [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
        self.assertIn('id="awesome">Awesome</h1>', result)
        self.assertNotIn("![", result)

    def test_safe_html(self):
        self.assertEqual(site.inline('<script>alert("x")</script>'), '&lt;script&gt;alert("x")&lt;/script&gt;')

    def test_unsafe_link_rejected(self):
        for link in ("javascript:alert", "//evil.example/x", "https://u:p@example.com/x"):
            with self.subTest(link=link), self.assertRaises(ValueError):
                site.resolve_link(link)

    def test_nested_lists_valid(self):
        output = site.convert("# Test\n- One\n  - Nested\n- Two\n\nParagraph\n")
        self.assertEqual(check_content.Document(output).errors, [])
        self.assertIn("</li></ul>", output)

    def test_ordered_lists(self):
        output = site.convert("# Test\n1. First\n2. Second\n\n3. Third\n")
        self.assertIn("<ol>", output)
        self.assertEqual(output.count("<li>"), 3)
        self.assertEqual(check_content.Document(output).errors, [])

    def test_changed_list_type(self):
        output = site.convert("# Test\n- Bullet\n1. Number\n")
        self.assertIn("</ul>", output)
        self.assertIn("<ol>", output)
        self.assertEqual(check_content.Document(output).errors, [])

    def test_bad_indentation_rejected(self):
        for text in ("- One\n   - Bad", "- One\n    - Skipped"):
            with self.assertRaises(ValueError):
                site.convert(text)

    def test_code_fence(self):
        output = site.convert('# Test\n```json\n{"x": "<>&"}\n```\n')
        self.assertIn('<pre><code class="language-json">', output)
        self.assertIn('&lt;&gt;&amp;', output)
        self.assertEqual(check_content.Document(output).errors, [])

    def test_unclosed_fence_rejected(self):
        with self.assertRaises(ValueError):
            site.convert("```python\nprint(1)")

    def test_table(self):
        output = site.convert("# Test\n| A | B |\n| --- | --- |\n| One | Two |\n")
        self.assertIn('<th scope="col">A</th>', output)
        self.assertIn('<td>Two</td>', output)
        self.assertEqual(check_content.Document(output).errors, [])

    def test_bad_table_rejected(self):
        with self.assertRaises(ValueError):
            site.convert("| A | B |\n| --- | --- |\n| One |\n")

    def test_markdown_link_to_published_page(self):
        self.assertEqual(site.resolve_link("../README.uz.md#modellar", "guides/test.md"), site.SITE_URL + "uz/#modellar")

    def test_link_to_repo_data(self):
        self.assertEqual(site.resolve_link("cases.jsonl", "evaluations/README.md"), site.REPO_URL + "/blob/main/evaluations/cases.jsonl")

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            site.resolve_link("../../etc/passwd")

    def test_metadata_manifest_is_unique(self):
        self.assertEqual(len({p["source"] for p in site.PAGES}), len(site.PAGES))
        self.assertEqual(len({site.page_url(p) for p in site.PAGES}), len(site.PAGES))
        self.assertEqual(len({p["title"] for p in site.PAGES}), len(site.PAGES))

    def test_sitemap_entries(self):
        from xml.etree import ElementTree
        output = site.expected_outputs()
        xml = ElementTree.fromstring(output["docs/sitemap.xml"])
        self.assertEqual(len(xml), len(site.PAGES))

    def test_build_reproducible(self):
        self.assertEqual(site.expected_outputs(), site.expected_outputs())


class LinkAuditTests(unittest.TestCase):
    def test_private_address_rejected(self):
        for ip in ("127.0.0.1", "10.0.0.1", "169.254.169.254", "::1"):
            with self.subTest(ip=ip), patch("socket.getaddrinfo", return_value=[(0, 0, 0, "", (ip, 443))]):
                with self.assertRaises(ValueError):
                    check_links.public_url("https://example.com/")

    def test_public_address_allowed(self):
        with patch("socket.getaddrinfo", return_value=[(0, 0, 0, "", ("93.184.216.34", 443))]):
            self.assertEqual(check_links.public_url("https://example.com/#x"), "https://example.com/")

    def test_non_web_url_rejected(self):
        with self.assertRaises(ValueError):
            check_links.public_url("file:///etc/passwd")

    def test_credentials_and_ports_rejected(self):
        for url in ("https://name:pass@example.com/", "http://example.com:8000/"):
            with self.assertRaises(ValueError):
                check_links.public_url(url)

    def test_invalid_url_reported(self):
        result = check_links.check_url("file:///etc/passwd", 1)
        self.assertEqual(result["status"], "review_required")
        self.assertIsNone(result["http_status"])


if __name__ == "__main__":
    unittest.main()
