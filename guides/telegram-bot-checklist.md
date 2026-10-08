# Launching an Uzbek Telegram bot: a practical checklist

[O‘zbekcha](telegram-bot-checklist.uz.md) · [Resource catalogue](../README.md) · [Choosing Uzbek AI](choosing-uzbek-ai.md)

Use this checklist before inviting real users to an Uzbek or Uzbek–Russian bot. It covers a small first release, including an optional AI component. It is a planning and acceptance guide, not a claim that any particular bot has passed these checks.

## 1. Define one complete user journey

Write down what a user should be able to finish: ask a documented question, submit a request, check an order, or book an available slot. Describe the starting point, required information, confirmation, saved result and next responsible person.

- Name the person who owns the bot, its content, technical support and ongoing costs.
- Separate facts and actions that must be deterministic from open-ended language tasks. Keep stock, prices, permissions and order status in the authoritative business system.
- Decide which actions need user confirmation. Show the actual details before creating a booking, changing a record or taking payment.
- Define when the bot asks a clarifying question, offers a human handoff, or says it cannot help.
- Keep a short list of features excluded from the first release. This makes testing and estimates more meaningful.

## 2. Set up ownership and protect credentials

Create and manage the bot through the official [BotFather](https://t.me/BotFather). Telegram's [bot tutorial](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) explains token creation and revocation. Treat a bot token like a password.

- Keep the production bot under an account controlled by the responsible owner; document how maintenance access will be handed over.
- Use separate test and production bots, credentials and data.
- Store bot tokens and model API keys in a secret store or protected runtime configuration. Never put them in source code, screenshots, public issues or client-side JavaScript.
- Redact credentials from logs and error reports, including URLs that contain tokens.
- Revoke an exposed token and replace it in the deployment. Removing it from a file does not invalidate a leaked copy.
- Give administrators only the access needed for their role.

## 3. Prepare Uzbek content and boundaries

- Offer a clear language choice. Preserve that choice across menus, errors and later messages.
- Test Uzbek Latin and Cyrillic, common apostrophe variants, mixed Uzbek–Russian wording, names and place names. Do not infer a person's preferred language from their name.
- Keep button labels short and consistent. Make “Back”, “Cancel” and “Talk to a person” behave predictably wherever they appear.
- Give an AI component approved reference material, with an owner and a review date. Test questions that the material cannot answer.
- Have a proficient Uzbek reader review important text. Mark examples as examples; do not publish invented testimonials, customer stories or evaluation results.
- Treat user messages and retrieved documents as untrusted input. Test attempts to make the bot expose another user's data, reveal secrets or perform an unauthorised action. Enforce permissions in application code, not only in a prompt.

For model or service selection, use the [AI guide](choosing-uzbek-ai.md) and [evaluation kit](../evaluations/README.md).

## 4. Make message processing recoverable

Choose either long polling or webhooks; Telegram does not allow both simultaneously. For webhooks, validate the `X-Telegram-Bot-Api-Secret-Token` header configured with `secret_token`. Use `update_id` to recognise repeated updates. These behaviours are documented in the [Bot API](https://core.telegram.org/bots/api#getting-updates).

- Record an update durably before acknowledging it when losing that update would lose a request or order.
- Make repeated deliveries and button taps safe: one intended action should create one business record. Use an application-level idempotency key for consequential writes.
- Put slow model calls and integration work in a bounded queue. Define timeouts, retry limits and a clear message when work cannot finish.
- Retry transient failures without creating duplicate bookings, charges or notifications. Distinguish “failed” from “result unknown”.
- Handle malformed input, unsupported attachments, blocked-bot errors and service outages without crashing the worker.
- Queue outgoing messages and handle rate-limit responses. Check Telegram's current [messaging limits](https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this) rather than hard-coding an assumed unlimited rate.
- If the bot is used in groups, verify which messages it receives under its actual permissions and [privacy mode](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get).

## 5. Make data handling understandable

Before asking for information, tell the user what is needed and why. Identify the bot operator and how to contact support. Explain if messages are sent to a model provider or another business system.

- Collect only the fields needed for the task. Use fictional data for development and acceptance tests.
- Define storage location, access roles, retention period and deletion procedure. Test deletion rather than merely promising it.
- Avoid logging full messages and attachments by default. Keep enough redacted diagnostic information to investigate failures.
- Separate consent for a requested service from consent for promotional messages. Provide a working way to stop optional notifications.
- Confirm that one user's history, documents and business records cannot appear in another user's chat.
- If taking payments, check Telegram’s separate documentation for [physical goods and services](https://core.telegram.org/bots/payments) and [digital goods and services](https://core.telegram.org/bots/payments-stars) before choosing the flow. Verify payment state on the backend; a screenshot or client-side success message is not proof of payment.

## 6. Run an acceptance test with recorded evidence

For each case, save the date, version, input, expected outcome, actual outcome and reviewer. The cases below are a starting point, not measured results or a complete security audit.

- **First visit:** `/start` explains the bot, presents the language choice and reaches the main task.
- **Language switch:** switching language also updates later validation errors and confirmation messages.
- **Missing information:** an incomplete request triggers a focused question instead of a fabricated answer.
- **Back and cancel:** navigation restores a sensible state; cancellation does not create a business record.
- **Repeated action:** a double tap, retry or duplicated update creates no duplicate order, lead or booking.
- **AI uncertainty:** an unsupported question receives a clear limitation or human handoff, without invented prices, availability or policy.
- **Isolation:** two test users cannot access each other's history or records, including by guessing an identifier.
- **Failure and restart:** model timeout, CRM outage and worker restart leave a recoverable state and a truthful status message.
- **Human handoff:** the designated person actually receives the request with the necessary context, and the user knows what happens next.
- **Abuse and spending:** unusually long inputs and repeated requests trigger your configured limits without exposing private information.

For payments or other consequential actions, add separate tests for duplicate callbacks, cancellation and an uncertain result. Do not launch that feature until its recovery process is clear.

## 7. Separate build cost from running cost

Ask for a breakdown based on your scope, not a single unexplained “bot price”:

- **One-time work:** journey design, Uzbek localisation, integrations, implementation, testing, deployment and handover.
- **Recurring infrastructure:** hosting, database, file storage, backups and monitoring.
- **AI usage:** input and output volume, retained conversation context, document retrieval, speech processing and retries where relevant.
- **Other providers:** CRM subscriptions, paid APIs, payment fees and any required licences.
- **People:** support, content updates, incident handling and later improvements.
- **Assumptions:** expected conversations, peak load, languages, included features, tax treatment and who pays each provider.

Use low, expected and high usage scenarios. Replace assumptions with actual pilot usage before increasing the audience, and set spending alerts and a hard application-level limit where possible.

For a worked scope breakdown, the Russian-language [Telegram bot cost calculator](https://gptbot.uz/ru/kalkulyator-stoimosti-telegram-bota/) separates development and estimated infrastructure costs. **Disclosure:** it is operated by GPTBot.uz, the team maintaining this catalogue. Its ranges are that team's planning estimates, not market benchmarks or a binding quote. Compare independent proposals using the same scope and exclusions; check model/API usage and other subscriptions separately.

## 8. Launch with an owner and a rollback plan

- Start with a small, agreed pilot audience and a defined review point.
- Record the version deployed, test evidence and unresolved limitations.
- Monitor failed requests, response time, handoffs and spending. For webhooks, inspect pending updates and delivery errors through [getWebhookInfo](https://core.telegram.org/bots/api#getwebhookinfo).
- Assign someone to receive alerts and decide when to pause the bot.
- Keep a tested way to disable consequential actions, switch to a human-support message and restore a known-good version.
- After an incident, fix the cause and rerun the affected tests before reopening the feature.

Do not mark the bot ready while credentials are exposed, user data crosses accounts, consequential actions can duplicate, or nobody owns failures. A working happy-path demo is only one part of launch readiness.

## About this guide

Prepared on 8 October 2026; Telegram-specific references and the calculator page were checked on that date. Provider behaviour and terms can change. GPTBot.uz is independent and is not affiliated with OpenAI or Telegram.

The repository's [CC0 licence](../LICENSE) applies to its own content. External services and software retain their own terms. Send corrections through the [contribution guidelines](../CONTRIBUTING.md).
