# Choosing AI for Uzbek: a practical guide

[O‘zbekcha](choosing-uzbek-ai.uz.md) · [Resource catalogue](../README.md) · [Evaluation kit](../evaluations/README.md)

Start with a task you can check. A service that produces fluent Uzbek may still misunderstand a name, change a number, or invent a source. This guide helps you choose candidates and record the evidence behind your choice. It contains no product rankings or measured comparisons.

## 1. Choose your route

- **Use AI today:** start with [apps and services](../README.md#apps-and-services). Compare chat assistants for drafting and explanations, translation tools for translation, and speech or OCR tools for recordings and scans. A chat subscription does not necessarily include API access.
- **Build an application:** browse [language models](../README.md#language-models) and [NLP tools](../README.md#nlp-libraries-and-tools). Decide whether you need a hosted API or a model you can run yourself. Confirm the integration and licence before building around it. For a Telegram project, use the [launch checklist](telegram-bot-checklist.md).
- **Find data or evaluate a model:** start with [datasets](../README.md#datasets), then [benchmarks](../README.md#benchmarks). Check the task, script, source, licence and train/test split. A translated dataset and one written originally in Uzbek answer different evaluation questions.
- **Learn:** use [courses and platforms](../README.md#courses-and-platforms). Pick one small outcome, such as a text classifier or a document-search prototype, and learn the tools needed to finish it.

## 2. Write a short task brief

Complete these fields before comparing tools:

- **Input:** text, scanned page, recording or structured data; usual length and file format.
- **Output:** the exact result needed, who reads it and where it will be used.
- **Language:** Uzbek Latin, Uzbek Cyrillic, mixed Uzbek–Russian, or another required combination. Note regional vocabulary and names.
- **Quality:** what must remain exact, such as dates, amounts, names, quotations or source links.
- **Privacy:** which information may leave your device or organisation, who approves it, and how long it may be stored.
- **Operations:** expected usage, acceptable waiting time, budget limit, and who handles mistakes.

For example, a draft FAQ answer reviewed by a person has different requirements from an assistant that changes an order in a CRM. Keep those two jobs separate in your brief.

## 3. Compare a small shortlist fairly

Choose two or three candidates from the relevant category. Use the same inputs, instructions and required output for each. Record the date, product or model version when available, settings, and whether browsing or other tools were enabled. Test the interface you actually intend to use: a website result does not establish the behaviour of an API or a locally run model.

For each candidate, keep the original response and note:

- **Meaning:** did it preserve the request, names, numbers and uncertainty?
- **Uzbek quality:** is the wording natural, is the requested script consistent, and are apostrophes and grammatical endings correct?
- **Task completion:** is the answer usable in the required format, without an extra manual reconstruction step?
- **Evidence:** do cited pages exist and support the claims? An impressive-looking citation is not verification.
- **Failure behaviour:** does it ask for missing information or admit a limit instead of inventing details?
- **Effort and cost:** how much review, correction, waiting and paid usage did this particular task require?

Ask a proficient Uzbek reader to review important public text. Spelling tools can help, but their approval does not verify factual accuracy. A short test is a screening exercise, not a general benchmark or proof of reliability.

## 4. Try these small language checks

The following are synthetic examples, not customer records or measured test results. Add examples from your own task after removing private information. The [evaluation kit](../evaluations/README.md) provides a place to develop a more repeatable comparison.

### Preserve facts while rewriting

Prompt: “Quyidagi xabarni mijozga mos, muloyim o‘zbekcha matnga aylantiring. Sana, vaqt va ismni o‘zgartirmang. Yangi va’da qo‘shmang: Dilnoza, uchrashuv 12-noyabr kuni soat 15:30 da. Hujjatlar hali tasdiqlanmadi.”

Check that the reply keeps Dilnoza, 12 November and 15:30, and does not claim that the documents are approved. Review whether the tone is polite without becoming unnecessarily formal.

### Keep the requested script

Prompt: “Faqat lotin yozuvida javob bering. Ushbu jumlani ma’nosini o‘zgartirmay lotinga o‘giring: Ўзбекистонда сунъий интеллект воситаларидан фойдаланиш.”

Expected text: “O‘zbekistonda sun’iy intellekt vositalaridan foydalanish.” Check for stray Cyrillic letters and altered meaning. Repeat with your actual names and terminology, using fictional personal details.

### Handle mixed language and missing facts

Prompt: “Mijoz ‘zakaz tayyormi, bugun olib ketsam bo‘ladimi?’ deb yozdi. Sizda buyurtma holati haqida ma’lumot yo‘q. Lotin yozuvida qisqa javob yozing va kerakli aniqlashtiruvchi savolni bering.”

A suitable answer asks for an order reference or another necessary detail. It must not promise that the order is ready or invent a pickup time. If your system can look up order status, test that integration separately.

### Stay within the supplied source

Give the tool a short, non-sensitive document and ask one answerable question and one question the document cannot answer. Check whether it separates supported information from missing information. For a search application, save the retrieved passages as well as the final answer so that retrieval errors and writing errors can be distinguished.

## 5. Check practical constraints before committing

- **Access:** confirm the service works from your location and on the intended device. Test the actual account or API plan you would use.
- **Privacy:** read the provider's current data-use and retention terms. Avoid uploading customer databases, credentials, medical information or other confidential material to an unapproved service. Use fictional or redacted examples during selection.
- **Licences:** check the model, base model, dataset and code separately. “Open weights” or a downloadable file does not establish permission for every use. Hugging Face explains where licences and evaluation information appear in [model cards](https://huggingface.co/docs/hub/model-cards).
- **Deployment:** for a local model, verify memory needs, dependencies and performance on your hardware. Review custom code before enabling options such as `trust_remote_code`.
- **Budget:** distinguish a free trial, recurring allowance, subscription and usage-based API. Verify the reset period, included usage, overage behaviour, taxes and payment availability with the provider. Do not assume that a catalogue label guarantees a particular limit.
- **Exit plan:** check whether you can export your work, remove stored data and switch providers without rebuilding the whole workflow.

## 6. Keep a decision record

- Chosen task and audience:
- Candidates and test date:
- Model or product versions and settings:
- Examples tested and failures found:
- Reviewer and remaining language issues:
- Privacy and licence checks still needed:
- Expected usage and spending limit:
- Selected option and reason:
- Conditions that would trigger another comparison:

Prefer the candidate that meets your actual requirements with an acceptable review burden. Recheck after a model change, a new type of input, a material price change, or a failure that affects users.

## About this guide

Prepared on 8 October 2026. This catalogue is maintained by the GPTBot.uz team, which operates an independent AI service and is not affiliated with OpenAI. The same selection checks apply to GPTBot.uz and competing services; inclusion is not an endorsement or a comparative performance claim.

The repository's [CC0 licence](../LICENSE) applies to its own content. Linked services, models, datasets and code retain their own terms. Improvements and corrections are welcome through the [contribution guidelines](../CONTRIBUTING.md).
