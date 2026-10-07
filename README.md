# Awesome Uzbek AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of artificial intelligence resources for the Uzbek language: apps that work in Uzbek, open models and datasets, NLP tools, benchmarks, and places to learn and meet the community.

**O‘zbekcha:** Bu ro‘yxatda o‘zbek tili uchun sun’iy intellekt resurslari jamlangan: o‘zbek tilida ishlaydigan ilovalar, ochiq modellar va ma’lumotlar to‘plamlari, NLP vositalari, benchmarklar, o‘quv materiallari va hamjamiyatlar. Ro‘yxat ingliz tilida yuritiladi. Yangi manba taklif qilmoqchi bo‘lsangiz, [hissa qo‘shish qoidalari](#contributing) bilan tanishing.

This list is maintained by the GPTBot.uz team in Tashkent. GPTBot.uz is an independent AI chat service and is not affiliated with OpenAI. To keep the list fair, it links to our own pages no more than three times, and each of those entries is marked "Disclosure". Other services, including our competitors, are listed on the same terms, and suggestions are welcome.

Links and facts were last checked on 7 October 2026. Plans, prices and language support change often, so check each site before relying on it.

## Contents

- [Apps and Services](#apps-and-services)
  - [AI Chats and Assistants](#ai-chats-and-assistants)
  - [Translation](#translation)
  - [Speech-to-Text and Text-to-Speech](#speech-to-text-and-text-to-speech)
  - [Text Recognition (OCR)](#text-recognition-ocr)
  - [Writing Tools](#writing-tools)
  - [Telegram Bots](#telegram-bots)
- [Language Models](#language-models)
  - [Uzbek-Adapted LLMs](#uzbek-adapted-llms)
  - [Encoders and Seq2seq Models](#encoders-and-seq2seq-models)
  - [Embeddings and Retrieval](#embeddings-and-retrieval)
  - [Machine Translation Models](#machine-translation-models)
  - [Task-Specific Models](#task-specific-models)
- [NLP Libraries and Tools](#nlp-libraries-and-tools)
- [Datasets](#datasets)
  - [Pretraining Corpora](#pretraining-corpora)
  - [Instruction and Preference Data](#instruction-and-preference-data)
  - [Task Datasets](#task-datasets)
  - [Speech Datasets](#speech-datasets)
- [Benchmarks](#benchmarks)
- [Learning](#learning)
  - [Courses and Platforms](#courses-and-platforms)
  - [Guides in Uzbek](#guides-in-uzbek)
  - [Video Lessons](#video-lessons)
  - [Papers](#papers)
- [Community](#community)
  - [Communities and Telegram Channels](#communities-and-telegram-channels)
  - [Events and Competitions](#events-and-competitions)
  - [Government Programs](#government-programs)
  - [Research Groups](#research-groups)
  - [Open Data Projects](#open-data-projects)

## Apps and Services

Services that work in Uzbek, from international products with Uzbek support to tools built in Uzbekistan. Pricing labels: *Free*, *Freemium* (free tier plus paid plans), *Paid* and *Open source*. International chatbots usually write Uzbek less well than English or Russian, so check important texts with a spell checker such as Tahrirchi.

### AI Chats and Assistants

- [ChatGPT](https://chatgpt.com/) - OpenAI's assistant. Uzbekistan is on OpenAI's supported-countries list, and it can read and write Uzbek in Latin or Cyrillic script. Freemium.
- [Claude](https://claude.ai/) - Anthropic's assistant, available in Uzbekistan. It can work with Uzbek text, but Uzbek is not among the languages in Anthropic's published multilingual benchmarks. Requires an account. Freemium.
- [Gemini](https://gemini.google.com/) - Google's assistant. Google announced official Uzbek support in the Gemini app in November 2025, and Uzbek appears in its supported-languages list. Freemium.
- [GPTBot.uz](https://gptbot.uz/uz/gpt-uzbek-tilida/) - Browser AI chat in Uzbek (Latin) and Russian that works without sign-up. Text only, with a daily free limit and an optional paid package; answers come from third-party models through an API. Built by an independent team in Tashkent; it is not ChatGPT and is not affiliated with OpenAI. Disclosure: maintained by the GPTBot.uz team, which also maintains this list. Freemium.
- [Qwen Chat](https://chat.qwen.ai/) - Alibaba's chat assistant, usable without logging in. The Qwen3 model family lists Northern Uzbek among its 119 supported languages. Free.
- [Yandex Alisa](https://alice.yandex.uz/uz/) - Yandex's voice assistant has spoken Uzbek and Russian on Yandex smart speakers since September 2025. To turn it on, choose the O‘zbekcha + Ruscha option in the Dom s Alisoy app settings. Requires a Yandex smart speaker.

### Translation

- [DeepL](https://www.deepl.com/en/translator) - Uzbek is one of DeepL's text translation languages, available on the web, in the apps and through the API. Freemium.
- [Google Translate](https://translate.google.com/?sl=uz&tl=en) - Translates text, documents and websites between Uzbek and Google's other languages. Free.
- [Microsoft Translator](https://www.bing.com/translator) - Translates Uzbek (Latin) text in Bing, Edge and the Translator apps. Developers can use the same languages through the Azure AI Translator API. Free (the API is paid).
- [Tilmoch](https://tilmoch.ai/uz/translator) - AI translator from the Tashkent startup Tahrirchi, built for Uzbek, Karakalpak and other Turkic languages. It translates text in 16 languages and PDF/DOCX files, and transcribes audio (beta). Also available as a mobile app and an API. Freemium.
- [Yandex Translate](https://translate.yandex.com/) - Translates text, documents and websites between Uzbek and Russian, English and about 120 other languages. Free.

### Speech-to-Text and Text-to-Speech

- [Aisha AI](https://aisha.group/uz) - Tashkent voice-AI company. It offers Uzbek, Russian and English speech-to-text that identifies each speaker, natural Uzbek text-to-speech voices, meeting notes and voice agents, in a free web workspace (voicelab.uz/app) and an Android app. The API has a free tier, then pay-as-you-go in so‘m. Freemium.
- [Azure AI Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support) - Microsoft's speech API. It recognises Uzbek (uz-UZ) speech and has two Uzbek neural voices, Madina and Sardor. Paid API with a free tier.
- [ElevenLabs Scribe](https://elevenlabs.io/speech-to-text/uzbek) - Speech-to-text model that supports Uzbek among 99 languages, with speaker labels and timestamps. Freemium.
- [Google Cloud Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) - Cloud speech recognition API that supports Uzbek (uz-UZ). Paid API.
- [KotibAI](https://kotib.ai/uz) - Speech analytics for call centres and sales teams in Uzbek, Russian and English. It transcribes and scores calls and also offers AI voice agents. Business product with demos on request. Paid.
- [Muxlisa AI](https://muxlisa.uz/uz) - Speech-to-text and text-to-speech platform from the state IT company UZINFOCOM, with Uzbek and Karakalpak support. It has an online demo, an API and a meeting notetaker, and its voice interface is used in the MyGov chatbot. Free minutes on sign-up, then paid per minute.
- [Narakeet](https://www.narakeet.com/languages/uzbek-text-to-speech-uz/) - Turns text, slides and scripts into Uzbek voice-overs and narrated videos in the browser. Free trial, then paid.
- [OpenAI Whisper](https://github.com/openai/whisper) - Open-source multilingual speech recognition model that runs on your own computer. Uzbek is one of its languages; it is a general-purpose model, so test its accuracy on your own Uzbek recordings. Open source.
- [UzbekVoiceAI](https://uzbekvoice.ai/) - Uzbek and mixed Uzbek-Russian speech-to-text, plus text-to-speech in neutral, happy, angry and sad styles. UzbekVoice Studio adds subtitles and dubbing. Made by the MohirAI team. Paid, with a 10,000 so‘m bonus on sign-up.
- [Yandex SpeechKit](https://aistudio.yandex.ru/en/ai-speech) - Yandex's cloud speech API. It has an Uzbek (uz-UZ) recognition model and three Uzbek text-to-speech voices: Nigora, Zamira and Yulduz. Paid API.

### Text Recognition (OCR)

- [ABBYY FineReader PDF](https://pdf.abbyy.com/specifications/) - Desktop OCR and PDF editor that recognises Uzbek in both Latin and Cyrillic script. Paid, with a trial.
- [Google Cloud Vision OCR](https://docs.cloud.google.com/vision/docs/languages) - OCR API that lists Uzbek among its supported languages. Paid API.
- [Tesseract OCR models](https://github.com/tesseract-ocr/tessdata) - Trained data for the free Tesseract OCR engine, with models for Uzbek Latin (`uzb`) and Uzbek Cyrillic (`uzb_cyrl`). Open source.

### Writing Tools

- [Imlo.uz](https://imlo.uz/) - Uzbek spelling dictionary in Latin and Cyrillic script. It is not an AI tool, but it is handy for checking AI-written text. Free.
- [Tahrirchi](https://tilmoch.ai/uz/editor) - Uzbek checker for spelling, grammar, style and punctuation, with Latin-Cyrillic conversion that leaves names and brands unchanged. Also available as a Chrome extension and a Word add-in. Freemium.

### Telegram Bots

- [Mohir AI Bot](https://t.me/MohirAIChatBot) - Uzbek-language AI assistant "Mohira" from the MohirAI team behind UzbekVoiceAI, linked from uzbekvoice.ai. Pricing is not stated publicly.
- [Tahrirchi Bot](https://t.me/tahrirchi_uzbot) - Official Tahrirchi bot for checking and converting Uzbek text inside Telegram. Free.

## Language Models

Open models for Uzbek: Northern Uzbek in Latin and Cyrillic script, plus some Southern Uzbek and Karakalpak. Licenses are taken from each model card or repository; "License not stated" means none is given, so check with the authors before commercial use. Results quoted below are the authors' own.

### Uzbek-Adapted LLMs

- [alloma-8B-Instruct](https://huggingface.co/uzlm/alloma-8B-Instruct) - Llama 3.1 8B continually pretrained on 3.6B tokens (about one third Uzbek) with an Uzbek-adapted tokenizer, then instruction-tuned; [1B](https://huggingface.co/uzlm/alloma-1B-Instruct) and 3B versions exist. License: Llama 3.1 / 3.2 Community License.
- [Aya 101](https://huggingface.co/CohereLabs/aya-101) - Massively multilingual 13B instruction-following model from Cohere Labs; Uzbek is one of its 101 languages. License: Apache-2.0.
- [Llama-3.1-8B-Instruct-Uz](https://huggingface.co/behbudiy/Llama-3.1-8B-Instruct-Uz) - Llama 3.1 8B Instruct further tuned on Uzbek and English instruction data; the card reports translation, sentiment and news-classification scores. License: Llama 3.1 Community License.
- [mGPT-1.3B-uzbek](https://huggingface.co/ai-forever/mGPT-1.3B-uzbek) - Version of mGPT 1.3B with additional training on Uzbek text. License: MIT.
- [Mistral-7B-Instruct-Uz](https://huggingface.co/behbudiy/Mistral-7B-Instruct-Uz) - Mistral 7B Instruct v0.3 tuned for Uzbek by the Behbudiy team; a 12B [Mistral-Nemo-Instruct-Uz](https://huggingface.co/behbudiy/Mistral-Nemo-Instruct-Uz) is also published. License: Apache-2.0.
- [MustaqiLLM](https://huggingface.co/NeuronUz/MustaqiLLM) - 5.2B-parameter Uzbek chat and text-classification model (Latin and Cyrillic, custom architecture loaded with `trust_remote_code`); its card states it is not meant as a knowledge model. License: Apache-2.0.
- [NeuronAI-Uzbek](https://huggingface.co/NeuronUz/NeuronAI-Uzbek) - Qwen3-4B fine-tune with an extended Uzbek tokenizer; the card reports UzLiB benchmark results. License: Apache-2.0.
- [Qwen3-14B-Base-Uzbek-Cyrillic](https://huggingface.co/Just-Bax/Qwen3-14B-Base-Uzbek-Cyrillic) - Qwen3-14B base model adapted with LoRA for Uzbek text in Cyrillic script (text completion, not chat). License: Apache-2.0.
- [uzbek-gpt-103m](https://huggingface.co/IslombekT/uzbek-gpt-103m) - Small 103M-parameter decoder trained from scratch on Uzbek with its own 16k BPE tokenizer; a compact research baseline. License: Apache-2.0.

### Encoders and Seq2seq Models

- [BERTbek](https://huggingface.co/elmurod1202/bertbek-news-big-cased) - Cased BERT pretrained on a large Uzbek news corpus, with fine-tuned NER, POS, news and sentiment checkpoints from the same author ([paper](https://aclanthology.org/2024.sigul-1.5/)). License: MIT.
- [t5-base-uzbek](https://huggingface.co/rifkat/t5-base-uzbek) - T5-base trained from scratch on Uzbek for text-to-text tasks. License: Apache-2.0.
- [TahrirchiBERT](https://huggingface.co/tahrirchi/tahrirchi-bert-base) - 110M-parameter case-sensitive encoder pretrained on Latin-script Uzbek; a 67M [small](https://huggingface.co/tahrirchi/tahrirchi-bert-small) variant is also available. License: Apache-2.0.
- [UzBERT](https://huggingface.co/coppercitylabs/uzbert-base-uncased) - BERT base pretrained on about 625K Cyrillic-script Uzbek news articles ([paper](https://arxiv.org/abs/2108.09814)). License: MIT.
- [UzRoBERTa](https://huggingface.co/rifkat/uztext-3Gb-BPE-Roberta) - A RoBERTa model pretrained on about 3 GB of Uzbek text in Latin and Cyrillic script. License: Apache-2.0.
- [XLM-RoBERTa large](https://huggingface.co/FacebookAI/xlm-roberta-large) - Multilingual encoder whose pretraining data includes Uzbek; a common baseline for Uzbek NER and classification. License: MIT.

### Embeddings and Retrieval

- [Cross-lingual word embeddings for Turkic languages](https://github.com/elmurod1202/crosLingWordEmbTurk) - Aligned word embeddings and bilingual dictionaries for Uzbek, Turkish, Azerbaijani, Kazakh and Kyrgyz ([LREC 2020 paper](https://aclanthology.org/2020.lrec-1.499/)). License not stated.
- [fastText word vectors](https://fasttext.cc/docs/en/crawl-vectors.html) - Pretrained 300-dimensional Uzbek word vectors (`cc.uz.300`) trained on Common Crawl and Wikipedia. License: CC BY-SA 3.0.
- [LaBSE](https://huggingface.co/sentence-transformers/LaBSE) - Language-agnostic sentence embeddings covering Uzbek, often used for bitext mining. License: Apache-2.0.
- [ModernUzBERT](https://huggingface.co/Orzumurod/ModernUzBERT) - Uzbek sentence-embedding model based on ModernBERT, for semantic retrieval. License: Apache-2.0.
- [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large) - General multilingual text-embedding model that lists Uzbek among its languages. License: MIT.
- [uzbek-e5-small](https://huggingface.co/sukhrobnurali/uzbek-e5-small) - Version of multilingual-e5-small fine-tuned for Uzbek semantic search and Uzbek-English cross-lingual retrieval; see also the companion [uzbek-minilm](https://huggingface.co/sukhrobnurali/uzbek-minilm). License: MIT.

### Machine Translation Models

- [Dilmash](https://huggingface.co/tahrirchi/dilmash) - NLLB-based models translating between Karakalpak, Uzbek, Russian and English ([paper](https://arxiv.org/abs/2409.04269)). License: CC BY-NC 4.0.
- [Lutfiy](https://huggingface.co/tahrirchi/lutfiy) - NLLB-based translation model for Southern Uzbek (Arabic script), Northern Uzbek and English ([paper](https://arxiv.org/abs/2508.14586)). License: CC BY-NC 4.0.
- [MADLAD-400 MT](https://huggingface.co/google/madlad400-3b-mt) - Google's T5-based translation models for 400+ languages, including Uzbek. License: Apache-2.0.
- [NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M) - Meta's translation models for 200 languages, including Northern Uzbek (`uzn_Latn`); 1.3B and 3.3B variants also exist. License: CC BY-NC 4.0.

### Task-Specific Models

- [rubai-corrector-base](https://huggingface.co/islomov/rubai-corrector-base) - Uzbek and Russian text-correction model based on ByT5 base (punctuation, OCR and ASR typos, apostrophe normalization), with task-specific variants. License not stated.
- [UzABSA-LLM](https://huggingface.co/Sanatbek/UzABSA-LLM) - Qwen 2.5, Llama 3.1 and DeepSeek-R1-Distill models QLoRA-tuned for Uzbek aspect-based sentiment analysis. License: Apache-2.0.
- [uzbek-ner-xlmr-large](https://huggingface.co/UAzimov/uzbek-ner-xlmr-large) - XLM-R large fine-tuned for Uzbek named entity recognition on the Uzbek NER Gold dataset. License: MIT.
- [uzbek-news-category-classifier](https://huggingface.co/coppercitylabs/uzbek-news-category-classifier) - News topic classifier fine-tuned from UzBERT on about 60K Cyrillic-script news articles. License: MIT.
- [Uzbek-POS-Tagger-TahrirchiBERT](https://huggingface.co/MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT) - Part-of-speech tagger fine-tuned from TahrirchiBERT. License: Apache-2.0.

## NLP Libraries and Tools

- [apertium-uzb](https://github.com/apertium/apertium-uzb) - Apertium finite-state morphological transducer and linguistic data for Uzbek. License: GPL-3.0.
- [fitrat](https://github.com/tahrirchi/fitrat) - Python library with Latin-Cyrillic transliteration (HFST transducers with an exceptions list), language identification, tokenizers and morphological analysis. License: MIT.
- [Tahrirgoh](https://github.com/tahrirchi/tahrirgoh) - Web platform for collecting grammatical error correction (GEC) data. License: MIT.
- [Uzbek Hunspell spellchecker](https://uzbek-spell.github.io/) - Research spellchecker with Hunspell dictionary files and a proof-of-concept MS Office add-on.
- [Uzbek stopwords](https://github.com/elmurod1202/StopWords) - Automatically derived stopword lists for Uzbek. License: Apache-2.0.
- [uzbek-tagger-bert](https://github.com/MaksudSharipov/uzbek-tagger-bert) - Python library for transformer-based POS tagging of Uzbek. License: Apache-2.0.
- [uzbek-tokenizers](https://github.com/coppercitylabs/uzbek-tokenizers) - Sentence and word tokenizers for Uzbek. License not stated.
- [uzbek-wordlist](https://github.com/kmashrab/uzbek-wordlist) - Cyrillic-script Uzbek word list used for spell-check dictionaries. License: GPL-2.0.
- [UzbekStemmer](https://github.com/MaksudSharipov/UzbekStemmer) - Lexicon-free rule-based stemmer for Uzbek. License: MIT-style (see repository).
- [UzMorphAnalyser](https://github.com/UlugbekSalaev/UzMorphAnalyser) - Affix-based morphological analyser for Uzbek (stemming, lemmatization, analysis). License: MIT.
- [UzTransliterator](https://github.com/UlugbekSalaev/UzTransliterator) - Python package for transliteration between Cyrillic, current Latin and the proposed new Latin Uzbek alphabets, combining rules and statistics. License: MIT.
- [UzWordnet](https://github.com/LDKR-Group/UzWordnet) - Lexical-semantic database for Uzbek, compatible with Princeton WordNet ([paper](https://aclanthology.org/2021.gwc-1.2/)). License not stated in the repository.

## Datasets

Corpora and labelled data for training and evaluating Uzbek models. Check each card for terms before commercial use.

### Pretraining Corpora

- [CC-100](https://data.statmt.org/cc-100/) - Monolingual Common Crawl data used to train XLM-R, including Uzbek.
- [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) - Filtered multilingual web corpus with `uzn_Latn` and `uzn_Cyrl` subsets. License: ODC-By.
- [HPLT v2 cleaned](https://huggingface.co/datasets/HPLT/HPLT2.0_cleaned) - Large multilingual web-text release with an `uzn_Latn` subset. License: CC0 (see the card for terms).
- [MADLAD-400](https://huggingface.co/datasets/allenai/MADLAD-400) - Document-level multilingual Common Crawl corpus with clean and noisy Uzbek splits. License: ODC-By.
- [rubai-text-s60m](https://huggingface.co/datasets/islomov/rubai-text-s60m) - About 1.14M synthetic Uzbek question and passage pairs across 80 topics, generated by distillation from a large LLM. License: CC BY 4.0.
- [Uzbek Legal Corpus v1](https://huggingface.co/datasets/sukhrobnurali/uzbek-legal-corpus-v1) - Article-structured research snapshot of Uzbekistan's codes and Constitution taken from Lex.uz (not legal advice). License: Apache-2.0.
- [Uzbek Wikipedia dumps](https://dumps.wikimedia.org/uzwiki/) - Official Wikimedia database dumps of Uzbek Wikipedia. License: CC BY-SA.
- [UzBooks v2](https://huggingface.co/datasets/tahrirchi/uz-books-v2) - Nearly 40,000 OCRed Uzbek books, provided as Latin and Cyrillic transliterated splits. License: MIT.
- [UzCrawl](https://huggingface.co/datasets/tahrirchi/uz-crawl) - Web and Telegram crawl corpus of Uzbek from about 1.2 million sources (v2 updated to March 2024). License: Apache-2.0.

### Instruction and Preference Data

- [alpaca-cleaned-uz](https://huggingface.co/datasets/behbudiy/alpaca-cleaned-uz) - Alpaca-cleaned instructions machine-translated into Uzbek with Google Translate. License not stated.
- [DPO-uz-9k](https://huggingface.co/datasets/MLDataScientist/DPO-uz-9k) - About 9,000 preference pairs machine-translated into Uzbek for DPO training. License: Apache-2.0.
- [oasst2_uzbek](https://huggingface.co/datasets/MLDataScientist/oasst2_uzbek) - OpenAssistant OASST2 conversations machine-translated into Uzbek with NLLB-200 3.3B. License: Apache-2.0.
- [translation-instruction](https://huggingface.co/datasets/behbudiy/translation-instruction) - 20,000 English-Uzbek translation and cross-lingual instruction examples. License not stated.
- [uzbek-instruct-llm](https://huggingface.co/datasets/UAzimov/uzbek-instruct-llm) - 15,000+ Uzbek instruction records, mostly translated from existing instruction sets. License: Apache-2.0.

### Task Datasets

- [Dilmash corpus](https://huggingface.co/datasets/tahrirchi/dilmash) - Parallel corpora pairing Karakalpak with Uzbek, Russian and English. License: MIT.
- [Lutfiy corpus](https://huggingface.co/datasets/tahrirchi/lutfiy) - About 40,000 parallel sentences between Southern Uzbek and Northern Uzbek or English. License: MIT.
- [rubai-NER-150K-Personal](https://huggingface.co/datasets/islomov/rubai-NER-150K-Personal) - 142,704 synthetic Uzbek and Russian examples for detecting personal information (PII) entities. License: Apache-2.0.
- [SimRelUz](https://huggingface.co/datasets/elmurod1202/SimRelUz_semantic_evaluation_dataset) - 1,000+ Uzbek word pairs with human similarity and relatedness scores ([paper](https://aclanthology.org/2022.sigul-1.26/)). License not stated.
- [UD Uzbek-UT](https://universaldependencies.org/treebanks/uz_ut/index.html) - First Universal Dependencies treebank for Uzbek (500 news and fiction sentences); see also [UzUDT](https://universaldependencies.org/treebanks/uz_uzudt/index.html) and [TueCL](https://universaldependencies.org/treebanks/uz_tuecl/index.html). License: CC BY-SA 4.0.
- [Uzbek ABSA](https://huggingface.co/datasets/Sanatbek/aspect-based-sentiment-analysis-uzbek) - Aspect-based sentiment dataset of Uzbek reviews in SemEval-2014 format. License not stated.
- [Uzbek NER Gold](https://huggingface.co/datasets/uznlp-uz/uzbek_NER) - 4,176 sentences with BIO tags for person, organization, location, money, date and other entity types. License: CC BY 4.0.
- [Uzbek sentiment analysis](https://github.com/elmurod1202/uzbek-sentiment-analysis) - First annotated Uzbek sentiment dataset (app reviews) with baseline code. License not stated.
- [Uzbek text classification dataset](https://huggingface.co/datasets/murodbek/uz-text-classification) - 512,750 Latin-script news articles from 9 sites in 15 categories ([paper](https://arxiv.org/abs/2302.14494)). License not stated.
- [Uzbek zero-shot classification](https://huggingface.co/datasets/risqaliyevds/uzbek-zero-shot-classification) - Uzbek news texts labelled with 10 topic categories. License: MIT.
- [uzbek-embedding-pairs](https://huggingface.co/datasets/sukhrobnurali/uzbek-embedding-pairs) - 356K parallel and monolingual Uzbek sentence pairs for training embedding models. License: Apache-2.0.
- [Uzbek-Kazakh parallel corpus](https://huggingface.co/datasets/Sanatbek/uzbek-kazakh-parallel-corpora) - Parallel sentences for Uzbek-Kazakh machine translation. License not stated.
- [uzbek_ner](https://huggingface.co/datasets/risqaliyevds/uzbek_ner) - NER dataset in JSON with person, place, organization, date and other entity types. License: MIT.
- [UzbekLemmaStems-POS-Dataset](https://github.com/MaksudSharipov/UzbekLemmaStems-POS-Dataset) - POS-tagged dataset of Uzbek word lemmas and stems for morphology research. License: Apache-2.0.
- [UzbekPOS](https://huggingface.co/datasets/latofat/uzbekpos) - First UPOS-annotated Uzbek dataset (250 sentences in Latin and Cyrillic) from the BBPOS work ([paper](https://arxiv.org/abs/2501.10107)). License: Apache-2.0.

### Speech Datasets

- [FeruzaSpeech](https://arxiv.org/abs/2410.00035) - 60-hour Uzbek read-speech corpus with punctuation, casing and context (2024). See the paper for access terms.
- [USC: Uzbek Speech Corpus](https://arxiv.org/abs/2107.14419) - Open-source Uzbek speech-recognition corpus with 105 hours from 958 speakers and baseline experiments (2021). See the paper for access terms.
- [UzbekVoice dataset project](https://discourse.mozilla.org/t/creating-open-and-accessible-resources-for-uzbek-the-uzbekvoice-ai-project/112634) - Background on the open Uzbek text and voice dataset project (about 1,400 hours collected) by the team behind UzbekVoiceAI, told on the Mozilla Discourse forum.

## Benchmarks

- [Belebele](https://huggingface.co/datasets/facebook/belebele) - Multilingual reading-comprehension benchmark with an `uzn_Latn` subset. License: CC BY-SA 4.0.
- [FLORES+](https://huggingface.co/datasets/openlanguagedata/flores_plus) - Machine-translation evaluation set with Northern (`uzn_Latn`) and Southern (`uzs_Arab`) Uzbek; access requires accepting terms on Hugging Face. License: CC BY-SA 4.0.
- [Global PIQA](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-nonparallel) - Culturally specific physical commonsense benchmark with an Uzbek subset. License: CC BY-SA 4.0.
- [IdrockBench](https://github.com/idrock-ai/IdrockBench) - Evaluation suite for Uzbek LLMs (exam-based knowledge, reasoning, instruction following, translation) from the IDROCK AI Excellence Center at New Uzbekistan University. License: MIT.
- [INCLUDE](https://huggingface.co/datasets/CohereLabs/include-base-44) - Multilingual regional-knowledge exam benchmark with an Uzbek subset. License: Apache-2.0.
- [Kardeş-NLU](https://github.com/lksenel/Kardes-NLU) - Natural language understanding benchmark for five Turkic languages including Uzbek ([EACL 2024 paper](https://aclanthology.org/2024.eacl-long.100/)). License not stated.
- [MMLU-uz](https://huggingface.co/datasets/murodbek/MMLU-uz) - Machine-translated Uzbek MMLU that has not been human-reviewed, plus a [Lite](https://huggingface.co/datasets/murodbek/MMLU-Lite-uz) version. License: Apache-2.0.
- [SIB-200](https://huggingface.co/datasets/Davlan/sib200) - Topic classification benchmark built on FLORES-200, including `uzn_Latn`. License: CC BY-SA 4.0.
- [TUMLU](https://github.com/ceferisbarov/TUMLU) - Native (not translated) school-level knowledge benchmark for Turkic languages including Uzbek; [TUMLU-mini](https://huggingface.co/datasets/jafarisbarov/TUMLU-mini) is on Hugging Face ([paper](https://arxiv.org/abs/2502.11020)). License: CC BY 4.0 (dataset).
- [UzLiB](https://github.com/tahrirchi/uzlib) - Uzbek Linguistic Benchmark: multiple-choice questions on correct Uzbek spelling, usage and meaning, with evaluation code and a public leaderboard ([dataset](https://huggingface.co/datasets/tahrirchi/uzlib)). License: MIT.
- [WikiANN](https://huggingface.co/datasets/unimelb-nlp/wikiann) - Automatically annotated (silver) multilingual NER data with an Uzbek split. License not stated.
- [XL-Sum](https://huggingface.co/datasets/csebuetnlp/xlsum) - Abstractive summarization dataset of BBC articles with an Uzbek subset. License: CC BY-NC-SA 4.0.

## Learning

Where to learn AI in Uzbek. Paid resources are marked as paid.

### Courses and Platforms

- [AiStudy.uz](https://aistudy.uz/) - Free national online platform for AI basics in Uzbek from the Ministry of Digital Technologies, part of the national AI Leaders programme; the companion site [omp.aistudy.uz](https://omp.aistudy.uz/) teaches prompt writing to the general public.
- [Besh million sun’iy intellekt yetakchilari](https://aileaders.uz/) - Free national online learning platform (AI Leaders) run by the Digital Education Development Center, successor to "One Million Uzbek Coders" (uzbekcoders.uz now redirects here). Uzbek interface with AI, data and IT courses from partners such as Coursera and Alison; course language varies. Official Telegram: [@aileaders_uz](https://t.me/aileaders_uz).
- [Mohirdev](https://mohirdev.uz/) - Uzbek-language online IT school. Its courses include the six-month [Data sayns va sun’iy intellekt](https://mohirdev.uz/kasblar/data-science-va-suniy-intellekt/) program (Python, ML, deep learning, NLP) and a shorter [NLP course](https://mohirdev.uz/kasblar/nlp/). Telegram: [@mohirdev](https://t.me/mohirdev). Paid.
- [Xarita.ai](https://xarita.ai/) - Free community-built roadmaps in Uzbek for learning AI, with separate paths for developers and everyday users and links to free courses and books; started in 2026 by Google Developer Expert Adkham Zokhirov.
- [Yandex ML School Uzbekistan](https://mlschool.yandex.uz/) - Free, selective one-year machine learning program in Tashkent run with New Uzbekistan University; offline evening classes taught in English, with admission by online test, exam and interview.

### Guides in Uzbek

- [ChatGPT talabalar uchun: 20 usul va promptlar](https://gptbot.uz/uz/blog/chatgpt-talabalar-uchun/) - Uzbek guide to studying with an AI chat (explaining topics, notes, test practice, translation, fact-checking) with academic-honesty rules. Disclosure: maintained by the GPTBot.uz team; GPTBot.uz is an independent service, not affiliated with OpenAI.
- [ChatGPT uchun o‘zbek tilida 50 ta tayyor prompt](https://gptbot.uz/uz/blog/chatgpt-uzbek-tilida-promptlar/) - 50 ready-to-adapt Uzbek prompts for study, work, marketing, sales and everyday tasks; they work in any AI chat. Disclosure: maintained by the GPTBot.uz team.
- [O‘qituvchilar uchun 12 ta sun’iy intellekt vositasi](https://abt.uz/blog/oqituvchilar-uchun-talimni-yaxshilovchi-12-ta-eng-samarali-suniy-intellekt-vositasi) - Uzbek article for teachers on 12 AI tools for lesson planning and classroom work, published by abt.uz.
- [Sun’iy intellekt (O‘zbekcha Vikipediya)](https://uz.wikipedia.org/wiki/Sun%CA%BCiy_intellekt) - Uzbek Wikipedia overview of AI; the longer [Generativ sun’iy intellekt](https://uz.wikipedia.org/wiki/Generativ_sun%CA%BCiy_intellekt) article covers generative models. Both are open for anyone to improve.

### Video Lessons

- [Adkham Zokhirov](https://www.youtube.com/@zokhirov) - AI and ML tutorials, learning roadmaps and career advice, mostly in Uzbek, from a Google Developer Expert in machine learning. Telegram: [@adkham_zokhirov](https://t.me/adkham_zokhirov).
- [Machine Learning fanini o‘rganish (Machine Learning Lab)](https://www.youtube.com/playlist?list=PLm6Oe3KKPuWHdt2FxDJ3JSUF2LCalYSze) - Structured machine learning course in Uzbek (supervised and unsupervised learning, linear regression, cost function, gradient descent, coding sessions), 2022-2023; the channel also has a NumPy series.
- [Mohirdev on YouTube](https://www.youtube.com/@Mohirdev) - Uzbek IT-education channel with free intro videos for its data science and AI courses, lessons on using AI tools, meetups and interviews.
- [Sariq dev](https://www.youtube.com/@Sariqdev) - Channel of Mohirdev founder Anvar Narzullaev with a Data Science playlist, AI explainers and a weekly Uzbek AI news show. Telegram: [@sariqdev](https://t.me/sariqdev).
- [Sun’iy intellekt (Milliy ta’lim resurslari)](https://www.youtube.com/playlist?list=PLFRnhpV9odGBNt4Xm_dRcgsPeI9pPwzeK) - 21-lesson school-level series in Uzbek (history of AI, why it matters, neural networks, evolutionary methods, sensors) on the channel that publishes content produced by the Ministry of Preschool and School Education.
- [Sun’iy intellekt va PyTorch (AMDUz)](https://www.youtube.com/playlist?list=PLqWThajMX99UDVYl2_W2a7pTdmDfFSq9M) - 12-lesson Uzbek series (2020-2021) on machine learning and deep learning basics with Python and PyTorch.

### Papers

- [Cloud and On-Premises Deployment of Uzbek Legal RAG](https://arxiv.org/abs/2608.29284) - Lessons from running a retrieval-augmented legal question-answering assistant for Uzbek in the cloud and on premises (2026).
- [Creating a morphological and syntactic tagged corpus for the Uzbek language](https://arxiv.org/abs/2210.15234) - POS and syntactic tagset for building an annotated Uzbek corpus (2022).
- [Development of Word Embeddings for Uzbek Language](https://arxiv.org/abs/2009.14384) - First publicly available word2vec, GloVe and fastText vectors for Cyrillic-script Uzbek (2020).
- [Recent Advancements and Challenges of Turkic Central Asian Language Processing](https://arxiv.org/abs/2407.05006) - Survey of NLP resources and methods for Uzbek, Kazakh, Kyrgyz and Turkmen (2024).
- [Uzbek Cyrillic-Latin-Cyrillic Machine Transliteration](https://arxiv.org/abs/2101.05162) - Data-driven transliteration between the two Uzbek scripts (2021).
- [Uzbek Sentiment Analysis based on local Restaurant Reviews](https://arxiv.org/abs/2205.15930) - Restaurant-review sentiment dataset with baseline models (2022).
- [UzbekTagger: The rule-based POS tagger for Uzbek language](https://arxiv.org/abs/2301.12711) - 12-tag POS-annotated dataset balanced across 20 domains, plus a rule-based tagger (2023).

## Community

People and organisations building AI in Uzbekistan and for the Uzbek language.

### Communities and Telegram Channels

- [AICA](https://aica.uz/) - Central Asian Association for Artificial Intelligence, based in Tashkent; runs the AICA Awards and education programs and co-organizes the National AI Hackathon.
- [Data Community Uz](https://t.me/datacommunityuz) - Tashkent community for data engineers, analysts and ML practitioners with regular offline meetups; posts mostly in Russian.
- [Databek](https://t.me/databek) - Small open data and AI community that publishes Uzbek datasets on [Hugging Face](https://huggingface.co/databek) and shares data-engineering programs.
- [GDG Tashkent](https://gdg.community.dev/gdg-tashkent/) - Independent Google Developer Group with 13,000+ members; free Build with AI meetups, ideathons, hackathons and DevFest. Telegram: [@gdgtashkent](https://t.me/gdgtashkent).
- [Global AI Tashkent](https://globalai.community/chapters/tashkent) - First Global AI Community chapter in Central Asia, hosted by the Center for AI and Digital Economy Development under the Ministry of Digital Technologies; regular talks and events.
- [ML Community Uzbekistan](https://mlcommunity.uz/) - AI community started in 2021 at Inha University in Tashkent; runs meetups, educational programs and hackathons and co-organizes the National AI Hackathon. Telegram: [@mlc_uz](https://t.me/mlc_uz).

### Events and Competitions

- [AI Tinkerers Tashkent](https://tashkent.aitinkerers.org/) - Tashkent chapter of the global AI builders meetup, with live demos and technical talks rather than pitches.
- [ICTWEEK Uzbekistan](https://www.ictweek.uz/eng) - Annual national ICT week in Tashkent; the 2026 program included an AI ethics forum and the Future Intelligence Forum.
- [International Olympiad in Artificial Intelligence (IOAI)](https://ioai-official.org/) - AI olympiad for secondary-school students; in December 2025 Uzbekistan added it to the state list of international olympiads whose winners receive state incentives (Government resolution No. 797).
- [National AI Hackathon](https://www.it-park.uz/en/itpark/news/samarqandda-ikkinchi-milliy-ai-hackathon-bo-lib-o-tadi) - Nationwide series of regional AI hackathons (healthcare, education, entrepreneurship and other tracks) run by the Ministry of Digital Technologies, IT Park and partners since October 2025, with the final planned in Tashkent in December 2026.
- [President AI Award](https://awards.gov.uz/en/paia) - National competition for AI startups based in Uzbekistan (teams of 3-8 with a working prototype); winners receive investment, and applying is free.

### Government Programs

- [AI Development Strategy until 2030](https://lex.uz/docs/7159258) - Presidential resolution PQ-358 of 14 October 2024 with the national AI strategy, a 2024-2026 action plan and a list of datasets to be created; official text on Lex.uz in Uzbek and Russian, plus an unofficial English translation.
- [AI O‘zbekiston](https://ai.gov.uz/ai/uz) - National AI portal (ai.gov.uz) with news, research, education and state AI project sections; some sections are still being filled in.
- [IT Park Uzbekistan](https://www.it-park.uz/) - State technology park that runs residency, startup and education programs and co-organizes national AI hackathons and events.
- [Sun’iy intellekt (Ministry of Digital Technologies)](https://gov.uz/oz/digital/activity_page/sun-iy-intellekt) - Ministry page on AI policy, the 2030 strategy, related legal acts and AI news.

### Research Groups

- [Behbudiy Labs](https://huggingface.co/behbudiy) - Publishes Uzbek-tuned Llama and Mistral instruction models and Uzbek instruction, translation and sentiment datasets.
- [Elmurod Kuriyozov](https://github.com/elmurod1202) - Uzbek NLP researcher from Urgench State University whose repositories cover sentiment datasets, stop words, cross-lingual word embeddings and other Uzbek resources.
- [IDROCK AI Lab](https://github.com/idrock-ai) - AI lab at New Uzbekistan University; publishes IdrockBench for evaluating Uzbek language models and a prompt-optimization study on an Uzbek university-entrance benchmark.
- [ISSAI](https://issai.nu.edu.kz/) - Institute of Smart Systems and Artificial Intelligence at Nazarbayev University (Kazakhstan); released the open Uzbek Speech Corpus with Uzbek partners and works on speech and language technology for Turkic languages.
- [SIGTURK](https://sigturk.github.io/) - ACL Special Interest Group on Turkic Languages. Its workshops ([2024 proceedings](https://aclanthology.org/events/sigturk-2024/), [2026 proceedings](https://aclanthology.org/events/sigturk-2026/)) are the main venue for Turkic NLP, and the 2026 volume includes a five-language Turkic idiom benchmark that covers Uzbek.
- [Tahrirchi](https://huggingface.co/tahrirchi) - Tashkent team working on Uzbek and Turkic NLP (grammar correction, translation); released TahrirchiBERT, the UzLiB benchmark and the Dilmash translation models.
- [Uzbek LLM Lab](https://huggingface.co/uzlm) - Group adapting open LLMs to Uzbek (the alloma 1B-8B models) that also released an Uzbek text-to-speech model.

### Open Data Projects

- [Common Voice: Uzbek](https://commonvoice.mozilla.org/uz) - Record or validate Uzbek sentences for Mozilla's open speech dataset; no technical skills needed.

## Related Lists

- [Awesome Uzbek NLP](https://github.com/Abdusalom0v/awesome-uzbek-nlp) - Another curated list of Uzbek NLP datasets, models, tools and papers.

## Contributing

Suggestions are welcome, including services that compete with ones already listed. Please read the [contribution guidelines](CONTRIBUTING.md) before opening an issue or pull request.
