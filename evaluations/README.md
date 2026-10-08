# Uzbek AI Evaluation Starter Pack

**24 original, synthetic prompt cases. No models have been run, tested, ranked, or scored with this pack.**

Version: 0.1.0. Authored: 2026-10-08. This is a small, open inspection set for reproducible Uzbek-language checks, not a validated benchmark or a leaderboard. The content was AI-assisted and self-reviewed; independent native-speaker or expert review has not been completed.

Oʻzbekcha: bu toʻplam lotin va kirill yozuvi, apostroflar, ruscha-oʻzbekcha aralash xabarlar, mijoz bilan yozishmalar va aniq koʻrsatmalarga rioya qilishni tekshirish uchun tayyorlangan. Namunalar sunʼiy; ular haqiqiy mijoz yozishmalari emas.

## What it covers

Each category has three cases:

| Category | IDs | Focus |
| --- | --- | --- |
| script_conversion | 001–003 | Uzbek Latin/Cyrillic conversion; oʻ, gʻ, q, x, h, sh, ch |
| apostrophes | 004–006 | Explicit Unicode normalization; tutuq; keeping distinct words distinct |
| mixed_ru_uz | 007–009 | Russian–Uzbek mixed messages, extraction, negation |
| business_dialogue | 010–012 | Prices, stock uncertainty, delayed orders without invented promises |
| instruction_adherence | 013–015 | JSON, line format, instructions quoted inside data |
| name_number_preservation | 016–018 | Names, leading zeros, identifiers, decimal comma, protected script |
| grounded_abstention | 019–021 | Missing facts, unknown source recency, selective abstention |
| structured_reasoning | 022–024 | Simple totals, elapsed time, rule-based selection |

The full IDs are `uz-eval-001` through `uz-eval-024`. All facts necessary for answers are in the prompts. No provider, product, crawler, or website is rewarded. There are no promotional links in the test cases.

## Files

- [prompts.jsonl](prompts.jsonl): UTF-8, one JSON object per line
- [rubric.md](rubric.md): exact comparison rules, manual grading, limitations, reporting
- [tools/validate.py](tools/validate.py): Python standard-library validation and safe blank-run generation

The files need no API key, paid service, package installation, or network access. Model inference, if you choose to perform it later, may have a separate cost depending on the runner you select. The included script never calls a model or submits data anywhere. Reuse follows the repository's license; the pack introduces no separate paywall or access restriction.

## Record format

Each record has six top-level fields:

- `id`: stable case identifier
- `category`: one of the eight categories above
- `language`: input-language notation; `+` means the input is mixed, not a formal combined BCP 47 tag
- `input`: the exact user message to send to the model
- `expected_or_rubric`: `exact_text`, `json`, or `checklist` grading specification
- `notes`: evaluator-only context and edge cases

Input tags include `uz-Latn`, `uz-Cyrl`, `ru-Cyrl`, and `en`. The requested output language is stated inside each prompt. Do not send the expected answers, checklists, notes, or this documentation to the model.

## Quick local check

From the directory containing this README:

```bash
python3 tools/validate.py validate
python3 tools/validate.py init-run ./runs/my-first-run
```

The first command validates UTF-8 JSONL structure, unique IDs, exactly 24 cases, three cases in each category, and grading-specification structure. It prints the corpus SHA-256. It does not establish linguistic correctness or model quality.

The second command creates `metadata.json` and `responses.jsonl` in the chosen directory, with every result marked `not_run` and every output set to `null`. It refuses to overwrite either file. File creation is preparation only: it does not run or score a model.

After recording outputs, check the response-file structure:

```bash
python3 tools/validate.py check-responses ./runs/my-first-run/responses.jsonl
```

This checks completeness, IDs, statuses, and value types. It does not grade answer correctness. Keep run files out of public commits unless you intend to publish them and have checked them for unintended private data.

## Manual or local-model run procedure

1. Freeze the corpus version, SHA-256, and repository commit. Read the rubric before running. Do not change acceptable answers after seeing which model produced them.
2. Fill in the generated metadata: provider or local runner, exact model identifier, version/snapshot when available, UTC start date/time, interface/version, system instructions, tool access, and every exposed generation setting. For a local model also record weight revision, quantization, runtime version, and chat template. Use `unknown` or `not exposed` when necessary; never invent a version.
3. Use a new conversation or reset context for each case. Send the `input` value verbatim as one user message, with no examples or answer key. The core run uses no browsing, retrieval, or other tools. If your interface adds unavoidable defaults, record them.
4. Use one predeclared first attempt per case for a basic run. Where supported, a reasonable controlled setting is temperature 0, an output cap of at least 1024 tokens, and a fixed seed. Record actual settings, including unsupported controls. These settings do not guarantee identical outputs across runs.
5. Save the exact visible final response to `raw_output`; preserve Unicode, whitespace, JSON formatting, and any unwanted preamble. Set `status` to `completed` only when a model response exists. Record time and any truncation. Do not repair the answer before grading or collect private chain-of-thought.
6. On a transport or runner failure, use `status: "error"`, `raw_output: null`, and a short non-secret error description. Do not treat unavailable infrastructure as a model's incorrect answer. Preserve errors if rerunning; identify a new run or attempt instead of silently replacing a poor answer.
7. Apply [the rubric](rubric.md), recording each result and evidence. Have a qualified Uzbek reviewer resolve linguistic uncertainty before publishing comparative claims. Blind the rater to model identity where practical.
8. Report case-level outcomes, per-category counts, coverage, and limitations. Publish a full-pack pass rate only with 24 completed, graded cases under the same declared protocol. For partial work, show the completed/graded denominator and missing or error cases prominently.

A no-cost starting point is a manual run in an interface you already have access to, or an already-installed local model. No particular provider or hosted API is required or recommended by the test design.

## Writing and comparison conventions

This version deliberately uses the familiar apostrophe-based Latin forms `oʻ`, `gʻ`, `sh`, and `ch`, together with Uzbek Cyrillic. It is a versioned test convention, not a claim about the present legal status of alphabet reforms. Future writing-system changes should create a documented new version rather than silently changing an answer key.

Most linguistic comparisons accept common apostrophe glyph variants at the same position. They never remove apostrophes or equate `ot` with `oʻt`. Case 004 explicitly requests two Unicode code points; cases 016 and 017 explicitly preserve source strings. Those exact-character requirements must remain strict.

Script conversion is not always a context-free character substitution: borrowed words, names, and choices around е/ё/ю/я or signs can be ambiguous. These starter cases deliberately avoid many of those issues. For open-ended responses, accept natural equivalent Uzbek wording under the stated checks rather than requiring the example answer verbatim. See the rubric for details.

## Source and provenance

The prompts and fictional scenarios are original material, not scraped customer conversations. No sensitive customer data, credentials, phone numbers, or real transaction records are included. Names and order codes are synthetic; any resemblance is incidental.

The [1995 basic Uzbek spelling rules on LexUZ](https://lex.uz/docs/1625271) were consulted as a language reference for the apostrophe-based convention, the tutuq distinction, and letter spellings. This is not a claim of endorsement, legal review, or complete current-policy coverage. The exact Unicode convention in case 004 is specified by that prompt itself.

## Limits and contributions

Twenty-four public examples cannot establish broad Uzbek fluency, dialect coverage, speech quality, domain expertise, fairness, safety, or production readiness. These are short written tasks, mostly standard Uzbek, with only a small amount of Russian code-switching. They do not represent all regional or colloquial usage. Public examples may enter training data; use a separate private, independently reviewed holdout for serious comparisons.

Useful improvements include independently reviewed language corrections, additional regional examples with explicit acceptance rules, and documented failure cases. Preserve old IDs when correcting wording without changing the task; increment the version and document any answer-changing revision. Add new IDs for substantially different tasks. Report disputed judgments instead of forcing a single spelling preference into a model ranking.
