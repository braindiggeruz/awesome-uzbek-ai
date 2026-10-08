"""Offline Markdown, catalog parity, local link, HTML and metadata checks."""
import collections
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_site import BY_SOURCE, PAGES, ROOT, SITE_URL, convert, page_url, slugify

LINK = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
RESOURCE = re.compile(r"^- \[([^]]+)\]\((https?://[^)]+)\) - ", re.M)


def prose(text):
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)


def markdown_ids(text):
    counts, result = {}, set()
    for heading in re.findall(r"^#{1,6} (.+)$", prose(text), re.M):
        heading = re.sub(r"\s*\[!\[.*$", "", heading)
        slug = slugify(heading)
        count = counts.get(slug, 0); counts[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


class Document(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.canonicals, self.languages, self.alternates = [], [], [], [], []
        self.stack, self.errors, self.headings = [], [], []
        self.feed(text)
        self.close()
        if self.stack:
            self.errors.append(f"Unclosed HTML tags: {self.stack}")

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "html":
            self.languages.append(a.get("lang"))
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag == "h1":
            self.headings.append(tag)
        if tag == "link" and a.get("rel") == "canonical":
            self.canonicals.append(a.get("href"))
        if tag == "link" and a.get("rel") == "alternate":
            self.alternates.append((a.get("hreflang"), a.get("href")))
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Mismatched closing tag: {tag}, stack={self.stack}")
        else:
            self.stack.pop()


def check():
    errors = []
    paths = [ROOT / "README.md", ROOT / "README.uz.md", ROOT / "CONTRIBUTING.md", ROOT / "MAINTENANCE.md"]
    paths += sorted((ROOT / "guides").glob("*.md")) + sorted((ROOT / "evaluations").glob("*.md"))
    for path in paths:
        name = path.relative_to(ROOT).as_posix()
        if not path.exists():
            errors.append(f"Missing source: {name}"); continue
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            errors.append(f"Missing final newline: {name}")
        for n, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line or "\t" in line:
                errors.append(f"Whitespace: {name}:{n}")
        if text.count("```", 0) % 2:
            errors.append(f"Unbalanced fence: {name}")
        if len(re.findall(r"^# ", prose(text), re.M)) != 1:
            errors.append(f"Expected one h1: {name}")
        try:
            convert(text, name)
        except ValueError as e:
            errors.append(str(e))
        for url in LINK.findall(prose(text)):
            parts = urlsplit(url)
            if parts.scheme:
                if parts.scheme not in ("https", "http") or not parts.netloc or parts.username or parts.password:
                    errors.append(f"Unsafe/unsupported URL: {name}: {url}")
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not target.is_relative_to(ROOT):
                errors.append(f"Link outside repository: {name}: {url}"); continue
            if not target.exists():
                errors.append(f"Missing local target: {name}: {url}"); continue
            if parts.fragment and target.suffix == ".md" and unquote(parts.fragment) not in markdown_ids(target.read_text(encoding="utf-8")):
                errors.append(f"Missing Markdown anchor: {name}: {url}")
    en = RESOURCE.findall((ROOT / "README.md").read_text(encoding="utf-8"))
    uz = RESOURCE.findall((ROOT / "README.uz.md").read_text(encoding="utf-8"))
    en_urls = collections.Counter(url for _, url in en)
    uz_urls = collections.Counter(url for _, url in uz)
    if en_urls != uz_urls:
        errors.append(f"Catalog resource parity: English-only {list((en_urls - uz_urls).elements())}; Uzbek-only {list((uz_urls - en_urls).elements())}")
    if len(en) < 163:
        errors.append(f"Unexpected resource loss: {len(en)} entries; baseline 163")
    if len(en_urls) != len(en):
        errors.append("Duplicate primary resource URL in English catalog")
    output_pages = {page_url(p): p for p in PAGES}
    parsed = {url: Document((ROOT / "docs" / p["output"]).read_text(encoding="utf-8")) for url, p in output_pages.items()}
    for url, doc in parsed.items():
        p = output_pages[url]
        errors.extend(f'{p["output"]}: {x}' for x in doc.errors)
        if len(set(doc.ids)) != len(doc.ids):
            errors.append(f'Duplicate HTML id: {p["output"]}')
        if doc.canonicals != [url] or doc.languages != [p["lang"]] or len(doc.headings) != 1:
            errors.append(f'Canonical, language or h1 mismatch: {p["output"]}')
        siblings = [s for s in PAGES if s["group"] == p["group"]]
        expected = {(s["lang"], page_url(s)) for s in siblings} if len(siblings) > 1 else set()
        if expected:
            expected.add(("x-default", page_url(next(s for s in siblings if s["lang"] == "en"))))
        if set(doc.alternates) != expected:
            errors.append(f'Hreflang mismatch: {p["output"]}')
        for link in doc.links:
            parts = urlsplit(link)
            if link.startswith("#"):
                if unquote(parts.fragment) not in doc.ids:
                    errors.append(f'Missing HTML anchor: {p["output"]}: {link}')
            elif link.startswith(SITE_URL):
                target_url = link.split("#")[0].split("?")[0]
                if target_url not in parsed:
                    errors.append(f"Missing site route: {link}")
                elif parts.fragment and unquote(parts.fragment) not in parsed[target_url].ids:
                    errors.append(f"Missing cross-page HTML anchor: {link}")
    reviews = json.loads((ROOT / "data/reviews.json").read_text(encoding="utf-8"))
    for review in reviews["reviews"]:
        for key in ("resource_url", "reviewed_on", "method", "evidence_urls", "observation", "affiliation", "limitations"):
            if not review.get(key):
                errors.append(f"Review missing {key}")
    return errors, len(en), len(paths)


def main():
    errors, entries, sources = check()
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Passed: {sources} Markdown sources, {entries} resources in each language, {len(PAGES)} HTML pages, local links/anchors, metadata and review records.")


if __name__ == "__main__":
    main()
