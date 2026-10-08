# Contribution Guidelines

Thank you for improving Awesome Uzbek AI. Suggest a resource through an issue or pull request. Competing services are welcome and evaluated on the same terms as affiliated projects.

## What Belongs Here

- Resources useful to Uzbek speakers or people working on Uzbek: apps, models, datasets, NLP tools, benchmarks, learning materials and communities.
- International tools with documented Uzbek support or a clearly described, reproducible Uzbek test.
- Primary sources with enough public information to verify the description. Explain account requirements or gated access rather than implying unrestricted availability.

## What Does Not Belong Here

- Impersonation of ChatGPT, OpenAI or another company.
- Link farms, keyword-stuffed landing pages, referral links, URL shorteners or tracking parameters.
- Unsupported rankings, fabricated benchmark results, copied proprietary test content or unverified pricing promises.
- Telegram bots whose ownership cannot be verified through their maker's official site or repository.

## Adding or Updating an Entry

1. Search both catalogs for duplicates and choose the correct section. Keep resource entries alphabetized within sections.
2. Use this format: `- [Name](https://example.com/) - Short factual description.`
3. Provide a primary evidence URL, the date you accessed it and the exact fact it supports in the issue or PR. A reachable URL alone is not a quality review.
4. State pricing cautiously. Use Free, Freemium, Paid or Open source only when current primary evidence supports the label; otherwise write "Pricing: check provider" or "Pricing not stated". Do not infer recurring free quotas from a trial.
5. For models and datasets, state the license from the card or repository, or "License not stated". A repository license does not necessarily settle the rights in its training data. Attribute reported benchmark results to their authors.
6. Disclose employment, ownership, funding or other affiliation in the PR and mark affiliated catalog entries with "Disclosure". No payment or backlink is required for inclusion.
7. Update README.md and README.uz.md together, preserving their matching primary URLs. If you cannot review the translation, say so. Do not claim native-speaker review unless it actually occurred.
8. Keep examples original and non-sensitive. Never paste real passwords, tokens, customer records or payment information into examples or test cases.
9. Record substantive fact checks in data/reviews.json with the source, date, method and limitations. Do not change an old date merely because HTTP returned 200.
10. Run the checks below and mention any unverified stage in your PR.

## Checks

```sh
python scripts/build_site.py
python scripts/build_site.py --check
python scripts/check_content.py
python evaluations/tools/validate.py validate
python -m unittest discover -s tests -v
```

See the [maintenance guide](MAINTENANCE.md) for optional external-link audits and the meaning of each check. The deterministic checks use Python's standard library and need no API keys.

## Writing and Review

Descriptions should be concise, factual and free of sales language. Uzbek examples in this repository normally use ‘ in o‘ and g‘ and ’ for tutuq belgisi. This is the repository's writing convention, not a claim about every accepted spelling or a Unicode-normalization rule for all data. Preserve original resource names and test inputs when those distinctions matter.

A reviewer should check the primary evidence, language, license context and affiliation. For material catalog updates, review both language versions. Editorial and native-speaker review are separate from automated checks.

## Broken Links and Corrections

Open an issue with the exact URL, what you observed and when. Authentication, throttling and bot-blocking errors need inspection before a resource is removed. Project owners may request corrections or removal; ownership does not entitle a project to a favorable ranking.

## O‘zbekcha

Yangi manba yoki tuzatish uchun issue yoki pull request yuboring. Birlamchi manba havolasi, uni ko‘rgan sana, tekshirilgan da’vo va loyihaga aloqangizni ko‘rsating. Inglizcha va o‘zbekcha ro‘yxatdagi havolalar mos bo‘lsin. Tarjimani ona tilida so‘zlashuvchi kishi tekshirmagan bo‘lsa, buni ochiq yozing. HTTP javobi vositaning sifatini tasdiqlamaydi.
