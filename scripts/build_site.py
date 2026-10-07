"""Build docs/index.html (the GitHub Pages site) from README.md.

Usage: python scripts/build_site.py

Standard library only. It understands the small Markdown subset used in
README.md: headings, paragraphs, one blockquote, nested "- " lists, links,
**bold**, *emphasis* and `code`. Run it after every README change.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://braindiggeruz.github.io/awesome-uzbek-ai/"
REPO_URL = "https://github.com/braindiggeruz/awesome-uzbek-ai"
LAST_CHECKED = "2026-10-07"
TITLE = "Awesome Uzbek AI: models, datasets, apps and courses for Uzbek"
DESCRIPTION = (
    "A curated, link-checked list of AI resources for the Uzbek language: "
    "apps that work in Uzbek, open models and datasets, NLP tools, benchmarks, "
    "courses and communities."
)
UZ_HINTS = re.compile(r"[‘’]|\b(uchun|tilida|fanini|yetakchilari|intellekt|Vikipediya)\b")


def slugify(text):
    """Approximate GitHub heading anchors."""
    text = text.lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def inline(text):
    """Convert inline Markdown to HTML."""
    out = []
    pos = 0
    pattern = re.compile(
        r"`(?P<code>[^`]+)`"
        r"|\[(?P<label>[^\]]+)\]\((?P<url>[^)\s]+)\)"
        r"|\*\*(?P<strong>[^*]+)\*\*"
        r"|\*(?P<em>[^*]+)\*"
    )
    for m in pattern.finditer(text):
        out.append(html.escape(text[pos:m.start()], quote=False))
        if m.group("code") is not None:
            out.append("<code>%s</code>" % html.escape(m.group("code"), quote=False))
        elif m.group("label") is not None:
            label, url = m.group("label"), m.group("url")
            if not re.match(r"https?://|#", url):
                url = "%s/blob/main/%s" % (REPO_URL, url)
            lang = ' lang="uz"' if UZ_HINTS.search(label) else ""
            out.append('<a href="%s"%s>%s</a>' % (html.escape(url), lang, inline(label)))
        elif m.group("strong") is not None:
            out.append("<strong>%s</strong>" % inline(m.group("strong")))
        else:
            out.append("<em>%s</em>" % inline(m.group("em")))
        pos = m.end()
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


def convert(markdown):
    lines = markdown.splitlines()
    body = []
    list_depth = 0  # number of open <ul>
    item_open = [False] * 4
    para = []

    def flush_para():
        if para:
            text = " ".join(para)
            if text.startswith("**O‘zbekcha:**"):
                body.append('<p lang="uz" class="uz">%s</p>' % inline(text))
            else:
                body.append("<p>%s</p>" % inline(text))
            para.clear()

    def close_lists(to_depth):
        nonlocal list_depth
        while list_depth > to_depth:
            if item_open[list_depth]:
                body.append("</li>")
                item_open[list_depth] = False
            body.append("</ul>")
            list_depth -= 1

    for line in lines:
        if not line.strip():
            flush_para()
            continue
        list_match = re.match(r"^( *)- (.*)$", line)
        if line.startswith("# "):
            flush_para(); close_lists(0)
            title = re.sub(r"\s*\[!\[.*$", "", line[2:]).strip()
            body.append("<h1>%s</h1>" % html.escape(title))
        elif line.startswith("## ") or line.startswith("### "):
            flush_para(); close_lists(0)
            level = 2 if line.startswith("## ") else 3
            text = line[level + 1:].strip()
            body.append('<h%d id="%s">%s</h%d>' % (level, slugify(text), html.escape(text), level))
        elif line.startswith("> "):
            flush_para(); close_lists(0)
            body.append('<p class="lead">%s</p>' % inline(line[2:]))
        elif list_match:
            flush_para()
            depth = len(list_match.group(1)) // 2 + 1
            if depth > list_depth:
                while list_depth < depth:
                    body.append("<ul>")
                    list_depth += 1
                    item_open[list_depth] = False
            else:
                close_lists(depth)
                if item_open[depth]:
                    body.append("</li>")
            body.append("<li>%s" % inline(list_match.group(2)))
            item_open[depth] = True
        else:
            close_lists(0)
            para.append(line.strip())
    flush_para()
    close_lists(0)
    return "\n".join(body)


def main():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    content = convert(readme)
    # Split the generated HTML into the intro (up to Contents) and the rest
    head_part, _, rest = content.partition('<h2 id="contents">')
    content = head_part + '<nav aria-label="Contents"><h2 id="contents">' + rest.replace(
        '<h2 id="apps-and-services">', '</nav>\n<h2 id="apps-and-services">', 1)
    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Awesome Uzbek AI",
        "description": DESCRIPTION,
        "url": SITE_URL,
        "inLanguage": "en",
        "dateModified": LAST_CHECKED,
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
    }, ensure_ascii=False)
    favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
               "%3Crect width='32' height='32' rx='7' fill='%230b7a5c'/%3E%3Ctext x='16' y='22' "
               "font-family='Arial' font-size='15' font-weight='700' fill='white' text-anchor='middle'%3EUz%3C/text%3E%3C/svg%3E")
    page = TEMPLATE.format(
        title=html.escape(TITLE),
        description=html.escape(DESCRIPTION),
        site_url=SITE_URL,
        repo_url=REPO_URL,
        json_ld=json_ld,
        favicon=favicon,
        content=content,
        last_checked=LAST_CHECKED,
    )
    out = ROOT / "docs" / "index.html"
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(page)
    print("wrote", out)


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{site_url}">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="website">
<meta property="og:title" content="Awesome Uzbek AI">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{site_url}">
<link rel="icon" href="{favicon}">
<script type="application/ld+json">{json_ld}</script>
<style>
:root {{
  --bg: #fbfbf8; --fg: #1d1f1e; --muted: #5a605d; --line: #dfe2dc;
  --link: #075e8c; --accent: #0b7a5c; --code: #eef0ea;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #141716; --fg: #e8ebe7; --muted: #a3aaa5; --line: #2f3532;
    --link: #7cc4ef; --accent: #4cc39c; --code: #222725;
  }}
}}
* {{ box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font: 16px/1.6 system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", sans-serif;
}}
main {{ max-width: 48rem; margin: 0 auto; padding: 24px 16px 48px; }}
h1 {{ font-size: 2rem; line-height: 1.2; margin: 0.5rem 0 0.75rem; }}
h2 {{ font-size: 1.4rem; margin: 2.5rem 0 0.5rem; padding-top: 0.5rem; border-top: 1px solid var(--line); }}
h3 {{ font-size: 1.1rem; margin: 1.75rem 0 0.25rem; color: var(--accent); }}
p, li {{ overflow-wrap: anywhere; }}
.lead {{ font-size: 1.1rem; color: var(--muted); margin-top: 0; }}
.uz {{ border-left: 3px solid var(--accent); padding-left: 12px; }}
a {{ color: var(--link); text-underline-offset: 2px; }}
a:hover {{ text-decoration-thickness: 2px; }}
ul {{ padding-left: 1.25rem; }}
li {{ margin: 0.4rem 0; }}
nav ul ul li {{ margin: 0.1rem 0; }}
code {{ font: 0.9em ui-monospace, SFMono-Regular, Consolas, monospace; background: var(--code); padding: 0.1em 0.3em; border-radius: 4px; }}
.meta {{ font-size: 0.9rem; color: var(--muted); }}
footer {{ margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--line); font-size: 0.9rem; color: var(--muted); }}
@media (max-width: 480px) {{
  h1 {{ font-size: 1.6rem; }}
  ul {{ padding-left: 1.1rem; }}
}}
</style>
</head>
<body>
<main>
<p class="meta"><a href="{repo_url}">Source on GitHub</a> &middot; Last checked {last_checked}</p>
{content}
<footer>
<p>Content is dedicated to the public domain under <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. This page is generated from <a href="{repo_url}/blob/main/README.md">README.md</a>; suggest changes through <a href="{repo_url}/issues">issues</a> or pull requests.</p>
</footer>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    main()
