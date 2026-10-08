# Maintenance and Verification

[Catalog](README.md) · [O‘zbekcha katalog](README.uz.md)

## Sources of Truth

- README.md is the English catalog; README.uz.md is its complete Uzbek translation. Keep primary resource URLs identical. Both currently contain 163 resource entries.
- Guides and evaluation documentation are authored in their own Markdown files. data/site.json defines their published routes, titles, descriptions and language pairs.
- docs/ is generated output. Never hand-edit its HTML. The build is deterministic and uses only Python's standard library.
- data/reviews.json records targeted editorial observations with a date, method, primary evidence and limitations. It is intentionally incomplete. Add records when a description is substantively checked, not just when the build runs.

## What a Check Means

- **Build check:** committed HTML and sitemap match the Markdown sources.
- **Content check:** Markdown structure, relative links, local anchors, English/Uzbek resource parity and generated metadata pass mechanical checks.
- **HTTP check:** a URL returned an HTTP response. A 200 response can still be a login wall, parked domain or changed product. HTTP success does not prove usefulness, security, Uzbek support, pricing or license correctness.
- **Editorial review:** a named claim was compared with a primary source and recorded with its limits. Provider claims remain provider claims unless independently tested.
- **Language review:** an Uzbek speaker has reviewed wording only if a specific review is documented. The new Uzbek translation and evaluation cases were prepared with AI assistance; native-speaker review remains outstanding.
- **Model evaluation:** a real model was run on the fixed prompts with recorded settings and reviewed outputs. No real-model results are included in this release.

No blanket "last checked" date is displayed. Page generation does not make old resource claims current. Sitemap URLs do not prove that a search engine has crawled or indexed a page.

## Local Checks

Run from the repository root with Python 3.12 or later:

```sh
python scripts/build_site.py
python scripts/build_site.py --check
python scripts/check_content.py
python evaluations/tools/validate.py validate
python -m unittest discover -s tests -v
```

The same deterministic checks run on pushes and pull requests. They require no secrets, paid APIs or model downloads.

## External Link Audit

```sh
python scripts/check_links.py --output reports/link-check.json
```

The report records the exact UTC audit time, source files, total coverage, response codes and redirects. A partial run with --limit is labeled partial. 404/410 responses are flagged as broken; authentication, throttling, network failures and other errors require manual review. A flagged link must be inspected before removing a useful resource. Do not equate bot blocking with an unavailable product.

The GitHub Actions workflow can also be started manually with its external_links option. That audit uploads the JSON report. It has no credentials beyond read-only repository access. It does not create commits, issues or pull requests. External availability is not a required PR check because it depends on other sites.

## Updating the Catalog

1. Use a primary product page, repository, model card or dataset card for material claims. Record the access date and what was actually checked.
2. Keep the entry factual; do not promote provider benchmark scores into an independent ranking. If sources conflict, say what is uncertain or remove the precise claim.
3. Mirror changed resource descriptions and URLs in both languages. Preserve all useful competitors and disclose affiliations.
4. Update the relevant guide only when the task or workflow changes. Avoid repeating promotional links.
5. Build, run checks, and inspect affected desktop and mobile pages. Native-speaker review and live deployment verification are separate tasks.
6. Open a draft pull request for review. Merging and deployment are separate decisions.

## Static Site

GitHub Pages serves the generated docs/ directory using the repository's existing configuration. Each translated page has its own canonical URL and reciprocal language alternates. The XML sitemap is generated at docs/sitemap.xml; no repository-subfolder robots.txt is added because it would not govern the host root.

The build does not deploy, contact model providers, execute downloaded model code or submit URLs to search engines. The existing Pages deployment runs only according to the repository's configured publishing settings.
