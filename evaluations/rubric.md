# Grading rubric

**Status: no model has been evaluated with this pack. There are no empirical scores to report.**

Use this rubric with version 0.1.0 of [prompts.jsonl](prompts.jsonl). The schema validator checks file integrity; it is not an automatic linguistic grader.

## Common rules

- Grade only the exact response saved in `raw_output` against its case. Do not use model identity, reputation, price, speed, or provider preference to decide correctness.
- Read the entire prompt and its notes. Keep strict output requirements separate from subjective style preferences. A polite, natural equivalent is valid when a checklist permits it.
- Keep all expected facts, protected names, numbers, negation, and uncertainty. Unsupported factual additions fail a relevant checklist check even when the prose is fluent.
- Extra introductions, explanations, Markdown fences, or apologies fail an exact-output contract. Do not silently remove them.
- Leading and trailing response whitespace, CRLF versus LF line endings, and Unicode NFC normalization are harmless unless a prompt explicitly says otherwise. Do not collapse internal whitespace, delete punctuation, reorder sentences, or normalize away meaningful characters.
- Missing output or an infrastructure error is ungraded and reduces coverage. A model-produced refusal, blank answer, wrong-language response, or truncated answer is an actual completed attempt; grade it against the prompt and record any truncation.
- If a genuinely valid answer exposes an answer-key ambiguity, mark it `needs_review`, explain the issue, and resolve it consistently across every model before publishing an aggregate. Do not label it a failure merely because it differs from a reference.

## Exact-text cases

An `exact_text` specification contains `expected` and `normalization`.

1. Normalize both texts to NFC.
2. Convert CRLF and CR to LF and trim only whitespace around the entire response.
3. For `nfc_trim`, compare all remaining characters exactly.
4. For `apostrophe_equivalent`, first map the five glyphs below to ASCII `'`, then compare all remaining characters exactly. Do not remove any sign.

Accepted equivalent glyphs for this mode:

| Glyph | Code point | Name |
| --- | --- | --- |
| ' | U+0027 | APOSTROPHE |
| ‘ | U+2018 | LEFT SINGLE QUOTATION MARK |
| ’ | U+2019 | RIGHT SINGLE QUOTATION MARK |
| ʻ | U+02BB | MODIFIER LETTER TURNED COMMA |
| ʼ | U+02BC | MODIFIER LETTER APOSTROPHE |

The equivalence applies only to cases that enable it. It is a narrow comparison convenience, not a general spelling rule. A grave accent/backtick, inserted spaces inside words, missing signs, or a different letter are not automatically equivalent. If an additional glyph should be accepted, document a versioned rule before comparison rather than making a provider-specific exception.

Case 004 must distinguish `ʻ` U+02BB in Oʻ/Gʻ from `ʼ` U+02BC in tutuq words because the prompt asks for those exact code points. NFC alone does not merge these characters. Cases 001 and 003 require the requested Uzbek Cyrillic letters, including ҳ rather than х when appropriate.

## JSON cases

A `json` specification contains `expected`, `string_normalization`, and `extra_keys: false`.

- Parse the entire output as one valid JSON value; surrounding whitespace is fine. Markdown fences and trailing commentary are not valid output for these cases.
- Reject duplicate object keys; a permissive parser silently keeping the last value would conceal a contract violation. Reject non-standard `NaN` and `Infinity`.
- Object key order and formatting whitespace outside strings do not matter. Array order does matter.
- Match the expected keys exactly, with no extra or missing keys. Do not normalize key spellings.
- Preserve JSON types. Strings are not numbers; `null` is not `"null"`; booleans must not be treated as numeric 0/1. Integer-only requests require a JSON integer token, not a decimal or exponent-form token.
- Compare string values after NFC normalization. For `string_normalization: "apostrophe_equivalent"`, additionally fold the five listed glyphs. Never trim or collapse whitespace inside a JSON string.
- Case 017 intentionally uses `string_normalization: "nfc"`: the source value `1 250 000 soʻm` and the initial zeros in `000731` must remain intact.

The expected JSON values in this version are small objects or arrays with no open-ended wording. In case 008 the prompt supplies the permitted payment labels, so an evaluator need not guess which synonyms to accept.

## Checklist cases

A `checklist` specification contains numbered `checks` and an illustrative `reference_answer`.

Grade each check as `pass`, `fail`, or `needs_review`. Add a short note quoting the relevant response segment or stating what is missing. The reference answer is one possible answer, never an exclusive wording requirement.

- Accept normal Uzbek paraphrases and ordinary apostrophe glyph variants unless the prompt protects a literal string.
- A response can use widely used borrowed words such as `kuryer` when appropriate. “Fully Uzbek” does not mean banning established loanwords. It does mean translating the Russian fragments and using the requested script.
- Do not penalize a natural difference in politeness formula, pronoun omission, or sentence order unless the prompt constrains it.
- For a two-sentence instruction, count full sentences in the visible answer. A semicolon does not create another sentence; a colon can introduce a phrase in the same sentence. Count questions or exclamations as sentences too. If abbreviations or malformed punctuation make the count genuinely ambiguous, flag review rather than rely on splitting on every period.
- “No added facts” still permits greetings or politeness when the requested sentence count and other constraints are satisfied. It forbids invented stock, dates, causes, commitments, and actions.
- Case 016 protects the exact string `Gʻayrat Joʻrayev`; do not change its apostrophe code points. In case 018, the protected Cyrillic name remains Cyrillic even though the rest of the answer is Latin. Obey the case-specific instruction before applying a blanket script rule.
- For grounded uncertainty, distinguish “not supplied” from “false.” An unknown stock level is not zero stock. Undated records do not establish which schedule is current. In case 021, only the unsupported holiday field should be `null`.

Linguistic judgments should be independently reviewed by qualified Uzbek readers before comparative publication. Record actual reviewers and qualifications only when known; this pack does not claim such review has already happened.

## Case outcome and aggregation

Use these case outcomes:

- `pass`: the exact/JSON comparison passes, or every checklist check passes
- `fail`: the output exists and violates at least one unambiguous required check
- `needs_review`: an unresolved linguistic or answer-key ambiguity prevents a fair decision
- `ungraded`: no completed output exists or no grading has been done

The main measure is strict case success, not an impressionistic fluency score. A checklist case with three passing checks and one failing check is a case failure; retain the check-level results as diagnostics. Do not mix a fraction of checks with whole-case pass counts in the same metric.

For a fully completed and adjudicated run:

- Full-pack success rate = passing cases / 24
- Each category success rate = passing cases / 3
- Always show the counts alongside percentages. With only three examples per category, one case changes a category rate by one third.

If any cases are missing, errored, ungraded, or under review, report coverage and outcomes rather than a purported full-pack score. A partial result may say “P passes / G graded completed cases; C of 24 responses collected; R cases under review,” using actual observed values. Do not put placeholder numbers in a leaderboard.

Do not claim statistical significance, broad capability superiority, or real-world reliability from this starter set. A single overall number hides different failure modes; show category and case-level evidence.

## Repeated runs and fair comparison

Declare repeated-run policy before collecting outputs. Use the same number of attempts, context reset, settings, tool policy, and scoring for every compared system. Never choose each model's best response after the fact.

Keep each repeated run in a separate directory with its own metadata and corpus hash. If the model is nondeterministic, report variation across runs. A seed and temperature 0 are useful controls when available, but they are not a reproducibility guarantee. Interface-specific hidden instructions and model updates can remain confounds; disclose them.

Do not use the tested model as its own sole judge. If using another model to assist grading later, record its identity and judging prompt, blind model names where possible, and have humans adjudicate uncertain language cases. No automated judge is included or run here.

## Recording outputs and judgments

`tools/validate.py init-run PATH` creates metadata and 24 blank response records. Fill the metadata before inference; keep all fields even when their values are `unknown`, `not exposed`, or `not applicable`.

For each response, record:

- Stable `case_id`, attempt number, status, and UTC collection time
- `raw_output` exactly as returned, or `null` for a not-run/error case
- Short `error` text only for infrastructure failure; omit credentials or private service details
- Whether the output was truncated
- `grading` with outcome, reviewer identifier, check-level judgments when applicable, and short evidence/notes

The blank template has `grading: null`. When grading is done, use an object with `outcome`, `reviewer`, `checks`, and `notes`. `checks` is an object keyed by C1/C2/etc. for checklist cases, or by `comparison` for exact-text/JSON cases. Each value is `pass`, `fail`, or `needs_review`. This is a recording convention, not a fabricated result.

Keep a copy of the original response and preserve any subsequent grading corrections as a documented revision. Do not save private chain-of-thought or unrelated account data.

## When to revise the pack

Record an issue when a prompt admits multiple valid answers that its grading rules cannot handle, when a supposedly natural sentence is disputed, or when an exact-character check measures typography more than the intended skill. Review changes blind to model identity where possible. Version answer-key changes and rerun comparisons against the same version; do not compare old and new scores as if the tasks were unchanged.
