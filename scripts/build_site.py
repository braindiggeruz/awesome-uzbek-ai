"""Deterministic, dependency-free Markdown-to-Pages build.

README.md and README.uz.md are the catalog sources; data/site.json maps prose
sources to routes. Supports headings, paragraphs, links, emphasis, code,
fenced blocks, blockquotes, ordered/unordered lists and simple pipe tables.
Raw HTML is escaped. Unsupported/malformed constructs fail validation.
"""
import argparse
import html
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "data/site.json").read_text(encoding="utf-8"))
SITE_URL = CONFIG["site_url"]
REPO_URL = CONFIG["repository_url"]
PAGES = CONFIG["pages"]
BY_SOURCE = {p["source"]: p for p in PAGES}
INLINE = re.compile(r"`(?P<code>[^`]+)`|\[(?P<label>[^\]]+)\]\((?P<url>[^)\s]+)\)|\*\*(?P<strong>[^*]+)\*\*|\*(?P<em>[^*]+)\*")
LIST = re.compile(r"^( *)(?:(?P<bullet>-) |(?P<number>\d+)\. )(?P<text>.*)$")


def slugify(text):
    """GitHub-style anchors for the heading subset used here."""
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[^\w\- ]", "", text.lower())
    return text.replace(" ", "-")


def page_url(page):
    return SITE_URL + page["output"].removesuffix("index.html")


def resolve_link(url, source="README.md"):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        if parts.scheme not in ("http", "https") or not parts.netloc or parts.username or parts.password:
            raise ValueError(f"Unsupported link: {url}")
        return url
    if url.startswith("#"):
        return url
    path = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parts.path)))
    if path.startswith("../") or path.startswith("/"):
        raise ValueError(f"Link leaves repository: {source}: {url}")
    fragment = "#" + parts.fragment if parts.fragment else ""
    query = "?" + parts.query if parts.query else ""
    if path in BY_SOURCE:
        return page_url(BY_SOURCE[path]) + query + fragment
    return f"{REPO_URL}/blob/main/{quote(path, safe='/')}" + query + fragment


def inline(text, source="README.md"):
    out, pos = [], 0
    for match in INLINE.finditer(text):
        out.append(html.escape(text[pos:match.start()], quote=False))
        if match.group("code") is not None:
            out.append("<code>" + html.escape(match.group("code")) + "</code>")
        elif match.group("label") is not None:
            url = resolve_link(match.group("url"), source)
            out.append(f'<a href="{html.escape(url, quote=True)}">{inline(match.group("label"), source)}</a>')
        elif match.group("strong") is not None:
            out.append("<strong>" + inline(match.group("strong"), source) + "</strong>")
        else:
            out.append("<em>" + inline(match.group("em"), source) + "</em>")
        pos = match.end()
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


def convert(markdown, source="README.md"):
    lines, body, para, stack, seen = markdown.splitlines(), [], [], [], {}

    def flush():
        if para:
            body.append("<p>" + inline(" ".join(para), source) + "</p>")
            para.clear()

    def close_lists(depth=0):
        while len(stack) > depth:
            body.append(f"</li></{stack.pop()}>")

    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip():
            flush()
            continue
        if line.startswith("```"):
            flush(); close_lists()
            language = line[3:].strip()
            if not re.fullmatch(r"[\w+-]*", language):
                raise ValueError(f"Invalid fence language in {source}")
            code = []
            while i < len(lines) and lines[i] != "```":
                code.append(lines[i]); i += 1
            if i == len(lines):
                raise ValueError(f"Unclosed code fence in {source}")
            i += 1
            klass = f' class="language-{language}"' if language else ""
            body.append(f"<pre><code{klass}>" + html.escape("\n".join(code)) + "</code></pre>")
            continue
        heading = re.match(r"^(#{1,6}) (.+)$", line)
        item = LIST.match(line)
        if heading:
            flush(); close_lists()
            level, text = len(heading[1]), heading[2]
            text = re.sub(r"\s*\[!\[.*$", "", text).strip()
            slug = slugify(text)
            count = seen.get(slug, 0); seen[slug] = count + 1
            anchor = f"{slug}-{count}" if count else slug
            body.append(f'<h{level} id="{anchor}">{inline(text, source)}</h{level}>')
        elif item:
            flush()
            if len(item[1]) % 2:
                raise ValueError(f"List indent must be two spaces in {source}: {line}")
            depth = len(item[1]) // 2 + 1
            kind = "ul" if item["bullet"] else "ol"
            if depth > len(stack) + 1:
                raise ValueError(f"List skips a level in {source}: {line}")
            close_lists(depth)
            if depth == len(stack) and stack[-1] != kind:
                close_lists(depth - 1)
            if depth > len(stack):
                start = f' start="{item["number"]}"' if kind == "ol" and item["number"] != "1" else ""
                body.append(f"<{kind}{start}>")
                stack.append(kind)
            else:
                body.append("</li>")
            body.append("<li>" + inline(item["text"], source))
        elif line.startswith("|") and i < len(lines) and re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?", lines[i]):
            flush(); close_lists()
            headers = [x.strip() for x in line.strip("|").split("|")]
            i += 1
            body.append('<div class="table-wrap" role="region" aria-label="Comparison table" tabindex="0"><table><thead><tr>')
            body.extend('<th scope="col">' + inline(x, source) + "</th>" for x in headers)
            body.append("</tr></thead><tbody>")
            while i < len(lines) and lines[i].startswith("|"):
                cells = [x.strip() for x in lines[i].strip("|").split("|")]
                if len(cells) != len(headers):
                    raise ValueError(f"Unequal table columns in {source}")
                body.append("<tr>" + "".join("<td>" + inline(x, source) + "</td>" for x in cells) + "</tr>")
                i += 1
            body.append("</tbody></table></div>")
        elif line.startswith("> "):
            flush(); close_lists()
            body.append('<blockquote><p>' + inline(line[2:], source) + "</p></blockquote>")
        elif line == "---":
            flush(); close_lists(); body.append("<hr>")
        else:
            close_lists()
            if line.startswith("|") or line.startswith("~~~"):
                raise ValueError(f"Unsupported Markdown block in {source}: {line}")
            para.append(line.strip())
    flush(); close_lists()
    return "\n".join(body)


CSS = """
:root{--bg:#fbfbf8;--fg:#1d1f1e;--muted:#525b55;--line:#d5ddd5;--link:#075e8c;--accent:#08684f;--code:#edf1eb}
@media(prefers-color-scheme:dark){:root{--bg:#141716;--fg:#e8ebe7;--muted:#b3bcb5;--line:#414c43;--link:#8bcdf4;--accent:#6ad7ad;--code:#252e28}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-padding-top:1rem}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}
main,.topbar{max-width:58rem;margin:0 auto;padding:1.25rem}main{padding-bottom:3rem}.topbar{display:flex;flex-wrap:wrap;gap:.5rem 1.2rem;border-bottom:1px solid var(--line)}.topbar a{padding:.25rem 0}.topbar [aria-current]{font-weight:700}
h1{font-size:2.1rem;line-height:1.2;margin:.8rem 0 1rem}h2{font-size:1.45rem;margin-top:2.5rem;border-top:1px solid var(--line);padding-top:.8rem}h3{font-size:1.15rem;margin-top:1.8rem;color:var(--accent)}p,li,h1,h2,h3{overflow-wrap:anywhere}a{color:var(--link);text-underline-offset:.18em}a:hover{text-decoration-thickness:.15em}a:focus-visible,button:focus-visible,[tabindex]:focus-visible{outline:3px solid var(--accent);outline-offset:4px}ul,ol{padding-left:1.4rem}li{margin:.5rem 0}li li{margin:.25rem 0}code{font:.9em ui-monospace,monospace;background:var(--code);padding:.1em .3em;border-radius:3px}pre{overflow:auto;padding:1rem;background:var(--code);border-radius:6px}pre code{padding:0}blockquote{margin:1rem 0;padding:.1rem 1rem;border-left:3px solid var(--accent);color:var(--muted)}.table-wrap{overflow-x:auto}table{border-collapse:collapse;min-width:100%}th,td{text-align:left;vertical-align:top;border:1px solid var(--line);padding:.6rem}th{background:var(--code)}footer{margin-top:3rem;border-top:1px solid var(--line);font-size:.9rem;color:var(--muted)}.skip{position:absolute;left:1rem;top:-10rem;background:var(--bg);padding:.6rem;z-index:2}.skip:focus{top:.5rem}.meta{color:var(--muted);font-size:.9rem}@media(max-width:480px){h1{font-size:1.7rem}main,.topbar{padding:1rem}ul,ol{padding-left:1.15rem}}
""".strip()


def render(page):
    lang, source, title, description = (page[x] for x in ("lang", "source", "title", "description"))
    url = page_url(page)
    siblings = [p for p in PAGES if p["group"] == page["group"]]
    alternates = "\n".join(f'<link rel="alternate" hreflang="{p["lang"]}" href="{page_url(p)}">' for p in siblings) if len(siblings) > 1 else ""
    if len(siblings) > 1:
        alternates += f'\n<link rel="alternate" hreflang="x-default" href="{page_url(next(p for p in siblings if p["lang"] == "en"))}">'
    nav = []
    for p in siblings:
        current = ' aria-current="page"' if p == page else ""
        label = "O‘zbekcha" if p["lang"] == "uz" else "English"
        nav.append(f'<a href="{page_url(p)}" hreflang="{p["lang"]}" lang="{p["lang"]}"{current}>{label}</a>')
    home = page_url(next(p for p in PAGES if p["group"] == "catalog" and p["lang"] == lang))
    nav.insert(0, f'<a href="{home}">{"Katalog" if lang == "uz" else "Catalog"}</a>')
    json_ld = json.dumps({"@context":"https://schema.org", "@type":page["type"], "name":title, "description":description, "url":url, "inLanguage":lang, "license":"https://creativecommons.org/publicdomain/zero/1.0/"}, ensure_ascii=False).replace("<", "\\u003c")
    text = (ROOT / source).read_text(encoding="utf-8")
    source_label = "GitHub’dagi manba" if lang == "uz" else "Source on GitHub"
    skip = "Asosiy mazmunga o‘tish" if lang == "uz" else "Skip to content"
    footer = "Mazmun CC0 1.0 asosida berilgan. Xato topsangiz, GitHub’da issue yoki pull request yuboring." if lang == "uz" else "Content is dedicated under CC0 1.0. Suggest corrections through GitHub issues or pull requests."
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<link rel="canonical" href="{url}">
{alternates}
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(description, quote=True)}">
<meta property="og:url" content="{url}">
<script type="application/ld+json">{json_ld}</script>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">{skip}</a>
<nav class="topbar" aria-label="{"Til va navigatsiya" if lang == "uz" else "Language and navigation"}">{" ".join(nav)}</nav>
<main id="main">
{convert(text, source)}
<footer><p>{footer} <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a></p>
<p><a href="{REPO_URL}/blob/main/{source}">{source_label}</a> · <a href="{REPO_URL}/issues">Issues</a></p></footer>
</main>
</body>
</html>
'''


def expected_outputs():
    outputs = {"docs/" + p["output"]: render(p) for p in PAGES}
    urls = "\n".join(f"  <url><loc>{html.escape(page_url(p))}</loc></url>" for p in PAGES)
    outputs["docs/sitemap.xml"] = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'
    outputs["docs/.nojekyll"] = ""
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed output differs from source; never writes")
    args = parser.parse_args()
    errors = []
    outputs = expected_outputs()
    stale = {str(p.relative_to(ROOT)) for p in (ROOT / "docs").rglob("*.html")} - outputs.keys()
    errors.extend("Unmapped generated HTML: " + p for p in sorted(stale))
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                errors.append("Out of date: " + name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
            print("wrote", name)
    if errors:
        raise SystemExit("\n".join(errors))
    if args.check:
        print(f"Generated output matches {len(PAGES)} Markdown sources and sitemap.")


if __name__ == "__main__":
    main()
