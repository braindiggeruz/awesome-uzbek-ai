# Awesome Uzbek AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) · O‘zbekcha · [Veb-sayt](https://braindiggeruz.github.io/awesome-uzbek-ai/)

O‘zbek tili uchun sun’iy intellekt resurslari: o‘zbek tilida ishlaydigan ilovalar, ochiq modellar va ma’lumotlar to‘plamlari, tabiiy tilni qayta ishlash (NLP) vositalari, baholash to‘plamlari, o‘quv materiallari va hamjamiyatlar.

Ro‘yxatni Toshkentdagi GPTBot.uz jamoasi yuritadi. GPTBot.uz mustaqil AI-chat xizmati bo‘lib, OpenAI bilan bog‘liq emas. Katalogdagi 3 ta resurs yozuvi shu jamoaga tegishli; ularning har birida manfaatdorlik ochiq ko‘rsatilgan. Telegram botini ishga tushirish bo‘yicha tekshirish ro‘yxatidagi jamoaga tegishli xarajat kalkulyatori katalog yozuvlaridan alohida ko‘rsatiladi va uning egasi ham ochiq aytiladi. Boshqa xizmatlar, jumladan raqobatchilar, bir xil mezonlar asosida kiritiladi. Yangi takliflar mamnuniyat bilan qabul qilinadi.

Tavsiflar manbalarning o‘z sahifalaridagi ma’lumotlarga asoslangan; barcha havolalar bir sanada tekshirilgani da’vo qilinmaydi. Aniq tekshiruv sanasi faqat unga dalil bo‘lsa qayd etiladi. Ro‘yxatga kiritilish sifat kafolati yoki mustaqil ekspertiza natijasi emas. Ayrim tavsiflar 2026-yil oktabrdagi dastlabki nashr uchun yig‘ilgan va bu yangilanishda qayta tekshirilmagan. Tariflar, narxlar, cheklovlar, litsenziyalar va til qo‘llovi o‘zgarishi mumkin, shuning uchun foydalanishdan oldin xizmatning o‘z sahifasini tekshiring. Muvaffaqiyatli HTTP tekshiruvi faqat sahifa javob berganini bildiradi, resurs ma’lumotlarining to‘g‘riligi yoki xavfsizligini tasdiqlamaydi. Hujjatlashtirilgan mazmun tekshiruvlari uchun [tekshiruv qaydlari](data/reviews.json)ga, tekshiruvlar nimani anglatishi uchun [yuritish qo‘llanmasi](MAINTENANCE.md)ga qarang. Ushbu tarjima sun’iy intellekt yordamida tayyorlangan va o‘zbek tilida ona tili darajasida so‘zlashuvchi muharrir tekshiruviga muhtoj.

## Boshlash uchun

- Talabalar: [ta’lim manbalari](#talim) va [o‘zbekcha qo‘llanmalar](#ozbekcha-qollanmalar)dan boshlang. AI javoblarini manbalar bilan tekshiring va ta’lim muassasangizning akademik halollik qoidalariga rioya qiling.
- Kontent yaratuvchilar: [nutqni matnga va matnni nutqqa aylantirish](#nutqni-matnga-va-matnni-nutqqa-aylantirish) hamda [yozish va tahrirlash vositalari](#yozish-va-tahrirlash-vositalari)ni ko‘ring.
- Dasturchilar: [til modellari](#til-modellari), [ma’lumotlar to‘plamlari](#malumotlar-toplamlari) va [baholash to‘plamlari](#baholash-toplamlari)ni o‘rganing; sinovlarni [baholash yo‘riqnomasi](evaluations/README.md) asosida qayd eting.
- Biznes vakillari: [o‘zbekcha AI vositasini tanlash qo‘llanmasi](guides/choosing-uzbek-ai.uz.md) yordamida vazifa, maxfiylik, xarajat va litsenziyalarni tekshiring. Telegram xizmatlari uchun [botni tekshirish ro‘yxati](guides/telegram-bot-checklist.uz.md)dan foydalaning.

## Mundarija

- [Boshlash uchun](#boshlash-uchun)
- [Ilovalar va xizmatlar](#ilovalar-va-xizmatlar)
  - [AI-chatlar va yordamchilar](#ai-chatlar-va-yordamchilar)
  - [Tarjima](#tarjima)
  - [Nutqni matnga va matnni nutqqa aylantirish](#nutqni-matnga-va-matnni-nutqqa-aylantirish)
  - [Matnni tanib olish (OCR)](#matnni-tanib-olish-ocr)
  - [Yozish va tahrirlash vositalari](#yozish-va-tahrirlash-vositalari)
  - [Telegram botlari](#telegram-botlari)
- [Til modellari](#til-modellari)
  - [O‘zbek tiliga moslashtirilgan LLMlar](#ozbek-tiliga-moslashtirilgan-llmlar)
  - [Enkoderlar va seq2seq modellari](#enkoderlar-va-seq2seq-modellari)
  - [Vektor ifodalar va qidiruv](#vektor-ifodalar-va-qidiruv)
  - [Mashina tarjimasi modellari](#mashina-tarjimasi-modellari)
  - [Muayyan vazifalarga mos modellar](#muayyan-vazifalarga-mos-modellar)
- [NLP kutubxonalari va vositalari](#nlp-kutubxonalari-va-vositalari)
- [Ma’lumotlar to‘plamlari](#malumotlar-toplamlari)
  - [Dastlabki o‘qitish korpuslari](#dastlabki-oqitish-korpuslari)
  - [Ko‘rsatmalar va afzalliklar ma’lumotlari](#korsatmalar-va-afzalliklar-malumotlari)
  - [Muayyan vazifalar uchun to‘plamlar](#muayyan-vazifalar-uchun-toplamlar)
  - [Nutq ma’lumotlari to‘plamlari](#nutq-malumotlari-toplamlari)
- [Baholash to‘plamlari](#baholash-toplamlari)
- [Ta’lim](#talim)
  - [Kurslar va platformalar](#kurslar-va-platformalar)
  - [O‘zbekcha qo‘llanmalar](#ozbekcha-qollanmalar)
  - [Videodarslar](#videodarslar)
  - [Ilmiy maqolalar](#ilmiy-maqolalar)
- [Hamjamiyat](#hamjamiyat)
  - [Hamjamiyatlar va Telegram kanallari](#hamjamiyatlar-va-telegram-kanallari)
  - [Tadbirlar va tanlovlar](#tadbirlar-va-tanlovlar)
  - [Davlat dasturlari](#davlat-dasturlari)
  - [Tadqiqot guruhlari](#tadqiqot-guruhlari)
  - [Ochiq ma’lumot loyihalari](#ochiq-malumot-loyihalari)
- [Aloqador ro‘yxatlar](#aloqador-royxatlar)
- [Hissa qo‘shish](#hissa-qoshish)

## Ilovalar va xizmatlar

O‘zbek tilida ishlaydigan xizmatlar: o‘zbek tilini qo‘llaydigan xalqaro mahsulotlardan tortib O‘zbekistonda yaratilgan vositalargacha. Narxlash belgilari: *Bepul*, *Freemium* (bepul daraja va pullik tariflar), *Pullik* va *Ochiq kodli*. Til sifati mahsulot, model va vazifaga qarab farq qiladi. Nomzod vositalarni bir xil o‘zbekcha namunalar bilan sinang va muhim matnlarni o‘zbek tilini biladigan kishiga tekshirtiring.

### AI-chatlar va yordamchilar

- [ChatGPT](https://chatgpt.com/) - OpenAI yordamchisi. O‘zbekiston OpenAI xizmatlari qo‘llab-quvvatlanadigan mamlakatlar ro‘yxatida bor; yordamchi o‘zbekcha lotin va kirill yozuvidagi matnni o‘qiydi va yozadi. Freemium.
- [Claude](https://claude.ai/) - Anthropic yordamchisi, O‘zbekistonda foydalanish mumkin. O‘zbekcha matn bilan ishlaydi, ammo o‘zbek tili Anthropic e’lon qilgan ko‘p tilli baholash natijalaridagi tillar qatoriga kiritilmagan. Hisob ochish talab etiladi. Freemium.
- [Gemini](https://gemini.google.com/) - Google yordamchisi. O‘zbek tili Gemini qo‘llab-quvvatlaydigan tillar ro‘yxatida bor. Freemium.
- [GPTBot.uz](https://gptbot.uz/uz/gpt-uzbek-tilida/) - Brauzerda ishlaydigan mustaqil AI-chat xizmati; o‘zbekcha (lotin) va ruscha matnli suhbatni taklif etadi, javoblar API orqali uchinchi tomon modellaridan olinadi. Joriy foydalanish imkoniyati, sinov cheklovlari va pullik shartlarni xizmat sahifasidan tekshiring; xizmat e’lon qilgan cheklov tavsiflarida o‘zaro nomuvofiqliklar kuzatilgan. Toshkentdagi mustaqil jamoa tomonidan yaratilgan; bu ChatGPT emas va OpenAI bilan bog‘liq emas. Manfaatdorlik haqida: xizmatni ushbu ro‘yxatni ham yuritadigan GPTBot.uz jamoasi boshqaradi. Narxlash: xizmat sahifasidan tekshiring.
- [Qwen Chat](https://chat.qwen.ai/) - Alibaba chat yordamchisi; tizimga kirmasdan foydalanish mumkin. Qwen3 modellar oilasi qo‘llab-quvvatlaydigan 119 til orasida shimoliy o‘zbek tili ham ko‘rsatilgan. Bepul.
- [Yandex Alisa](https://alice.yandex.uz/uz/) - Yandex aqlli karnaylarida o‘zbek va rus tillarida gapiradigan ovozli yordamchi. Uni yoqish uchun Dom s Alisoy ilovasi sozlamalarida O‘zbekcha + Ruscha variantini tanlang. Yandex aqlli karnayi talab etiladi.

### Tarjima

- [DeepL](https://www.deepl.com/en/translator) - O‘zbek tili DeepL matn tarjimasi tillari qatoriga kiradi; veb-sayt, ilovalar va API orqali foydalanish mumkin. Freemium.
- [Google Translate](https://translate.google.com/?sl=uz&tl=en) - O‘zbek tili va Google qo‘llaydigan boshqa tillar o‘rtasida matn, hujjat va veb-saytlarni tarjima qiladi. Bepul.
- [Microsoft Translator](https://www.bing.com/translator) - Bing, Edge va Translator ilovalarida o‘zbekcha (lotin) matnni tarjima qiladi. Dasturchilar shu tillardan Azure AI Translator API orqali foydalanishi mumkin. Bepul (API pullik).
- [Tilmoch](https://tilmoch.ai/uz/translator) - Toshkentdagi Tahrirchi startapining o‘zbek, qoraqalpoq va boshqa turkiy tillar uchun yaratilgan AI-tarjimoni. 16 tildagi matnni va PDF/DOCX fayllarini tarjima qiladi, audioni matnga o‘giradi (beta). Mobil ilova va API shaklida ham mavjud. Freemium.
- [Yandex Translate](https://translate.yandex.com/) - O‘zbek tili bilan rus, ingliz va yana taxminan 120 til o‘rtasida matn, hujjat va veb-saytlarni tarjima qiladi. Bepul.

### Nutqni matnga va matnni nutqqa aylantirish

- [Aisha AI](https://aisha.group/uz) - Toshkentdagi ovozli AI kompaniyasi. O‘zbek, rus va ingliz tillaridagi nutqni so‘zlovchilarni ajratgan holda matnga aylantirish, tabiiy o‘zbekcha ovozlar bilan matnni o‘qish, uchrashuv qaydlari va ovozli agentlarni taklif etadi. Bepul veb-ish maydoni (voicelab.uz/app) va Android ilovasi bor. APIda bepul daraja mavjud, undan keyin foydalanish hajmiga qarab so‘mda to‘lanadi. Freemium.
- [Azure AI Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support) - Microsoft nutq API xizmati. O‘zbekcha (uz-UZ) nutqni taniydi va Madina hamda Sardor nomli ikkita o‘zbekcha neyron ovozga ega. Bepul darajasi bor pullik API.
- [ElevenLabs Scribe](https://elevenlabs.io/speech-to-text/uzbek) - 99 til qatorida o‘zbek tilini ham qo‘llaydigan nutqni matnga aylantirish modeli; so‘zlovchi belgilari va vaqt belgilarini beradi. Freemium.
- [Google Cloud Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) - O‘zbek tilini (uz-UZ) qo‘llaydigan bulutli nutqni tanish API xizmati. Pullik API.
- [KotibAI](https://kotib.ai/uz) - Qo‘ng‘iroq markazlari va savdo jamoalari uchun o‘zbek, rus va ingliz tillaridagi nutq tahlili. Qo‘ng‘iroqlarni matnga o‘giradi va baholaydi, AI ovozli agentlarni ham taklif etadi. Biznes uchun mahsulot; namoyish so‘rov asosida beriladi. Pullik.
- [Muxlisa AI](https://muxlisa.uz/uz) - UZINFOCOM davlat IT kompaniyasining o‘zbek va qoraqalpoq tillarini qo‘llaydigan nutqni matnga va matnni nutqqa aylantirish platformasi. Onlayn namoyish, API va uchrashuv qaydlarini tayyorlovchi vositasi bor; ovozli interfeysi MyGov chatbotida ishlatiladi. Ro‘yxatdan o‘tishda bepul daqiqalar beriladi, keyin har daqiqa uchun to‘lanadi.
- [Narakeet](https://www.narakeet.com/languages/uzbek-text-to-speech-uz/) - Brauzerda matn, slayd va ssenariylarni o‘zbekcha ovozli yozuvlar hamda ovozlashtirilgan videolarga aylantiradi. Bepul sinovdan keyin pullik.
- [OpenAI Whisper](https://github.com/openai/whisper) - O‘z kompyuteringizda ishlaydigan ochiq kodli ko‘p tilli nutqni tanish modeli. O‘zbek tili ham mavjud; model umumiy maqsadli bo‘lgani uchun aniqligini o‘zbekcha yozuvlaringizda sinab ko‘ring. Ochiq kodli.
- [UzbekVoiceAI](https://uzbekvoice.ai/) - O‘zbekcha va o‘zbekcha-ruscha aralash nutqni matnga aylantiradi, Shoira va Jasur ovozlari bilan matnni o‘qiydi. UzbekVoice Studio subtitr va dublyaj imkoniyatlarini qo‘shadi. MohirAI jamoasi yaratgan. Pullik; ro‘yxatdan o‘tish bonusi mavjud (saytga qarang).
- [Yandex SpeechKit](https://aistudio.yandex.ru/en/ai-speech) - Yandex bulutli nutq API xizmati. O‘zbekcha (uz-UZ) nutqni tanish modeli va matnni nutqqa aylantiruvchi Nigora, Zamira hamda Yulduz nomli uchta ovozga ega. Pullik API.

### Matnni tanib olish (OCR)

- [ABBYY FineReader PDF](https://pdf.abbyy.com/specifications/) - O‘zbekcha lotin va kirill yozuvlarini taniydigan kompyuter uchun OCR va PDF muharriri. Pullik, sinov versiyasi bor.
- [Google Cloud Vision OCR](https://docs.cloud.google.com/vision/docs/languages) - Qo‘llab-quvvatlanadigan tillari orasida o‘zbek tili ham ko‘rsatilgan OCR API xizmati. Pullik API.
- [Tesseract OCR models](https://github.com/tesseract-ocr/tessdata) - Bepul Tesseract OCR tizimi uchun o‘qitilgan ma’lumotlar; o‘zbek lotin (`uzb`) va o‘zbek kirill (`uzb_cyrl`) yozuvlari modellari mavjud. Ochiq kodli.

### Yozish va tahrirlash vositalari

- [Imlo.uz](https://imlo.uz/) - Lotin va kirill yozuvidagi o‘zbekcha imlo lug‘ati. AI vositasi emas, ammo AI yozgan matnni tekshirishda foydali. Bepul.
- [Tahrirchi](https://tilmoch.ai/uz/editor) - O‘zbekcha imlo, grammatika, uslub va tinish belgilarini tekshiradi; nomlar va brendlarni o‘zgartirmasdan lotin-kirill o‘girish imkoniyati bor. Chrome kengaytmasi va Word qo‘shimchasi shaklida ham mavjud. Freemium.

### Telegram botlari

- [Mohir AI Bot](https://t.me/MohirAIChatBot) - UzbekVoiceAI ortidagi MohirAI jamoasining «Mohira» nomli o‘zbekcha AI yordamchisi; uzbekvoice.ai saytidan havola berilgan. Narxlar ommaga e’lon qilinmagan.
- [Tahrirchi Bot](https://t.me/tahrirchi_uzbot) - Telegram ichida o‘zbekcha matnni tekshirish va yozuvini o‘girish uchun rasmiy Tahrirchi boti. Bepul.

## Til modellari

O‘zbek tili uchun ochiq modellar: lotin va kirill yozuvidagi shimoliy o‘zbek tili, shuningdek ayrim janubiy o‘zbek va qoraqalpoq modellari. Litsenziyalar model kartasi yoki repozitoriydan olingan. «Litsenziya ko‘rsatilmagan» degani manbada litsenziya berilmaganini anglatadi; tijoriy foydalanishdan oldin mualliflardan aniqlashtiring. Quyida keltirilgan natijalarni model mualliflari e’lon qilgan.

### O‘zbek tiliga moslashtirilgan LLMlar

- [alloma-8B-Instruct](https://huggingface.co/uzlm/alloma-8B-Instruct) - Llama 3.1 8B asosida, o‘zbek tiliga moslashtirilgan tokenizator bilan 3,6 milliard tokenda (taxminan uchdan biri o‘zbekcha) qo‘shimcha dastlabki o‘qitishdan, keyin ko‘rsatmalar asosida moslashtirishdan o‘tgan model; [1B](https://huggingface.co/uzlm/alloma-1B-Instruct) va 3B versiyalari ham bor. Litsenziya: Llama 3.1 / 3.2 Community License.
- [Aya 101](https://huggingface.co/CohereLabs/aya-101) - Cohere Labs yaratgan 13 milliard parametrli, ko‘rsatmalarga amal qiladigan ko‘p tilli model; 101 tili orasida o‘zbek tili ham bor. Litsenziya: Apache-2.0.
- [Llama-3.1-8B-Instruct-Uz](https://huggingface.co/behbudiy/Llama-3.1-8B-Instruct-Uz) - O‘zbekcha va inglizcha ko‘rsatmalar ma’lumotlarida qo‘shimcha moslashtirilgan Llama 3.1 8B Instruct; model kartasida tarjima, hissiy munosabat tahlili va yangiliklarni tasniflash natijalari berilgan. Litsenziya: Llama 3.1 Community License.
- [mGPT-1.3B-uzbek](https://huggingface.co/ai-forever/mGPT-1.3B-uzbek) - O‘zbekcha matnda qo‘shimcha o‘qitilgan mGPT 1.3B versiyasi. Litsenziya: MIT.
- [Mistral-7B-Instruct-Uz](https://huggingface.co/behbudiy/Mistral-7B-Instruct-Uz) - Behbudiy jamoasi o‘zbek tiliga moslashtirgan Mistral 7B Instruct v0.3; 12B hajmli [Mistral-Nemo-Instruct-Uz](https://huggingface.co/behbudiy/Mistral-Nemo-Instruct-Uz) ham e’lon qilingan. Litsenziya: Apache-2.0.
- [MustaqiLLM](https://huggingface.co/NeuronUz/MustaqiLLM) - O‘zbekcha chat va matn tasnifi uchun 5,2 milliard parametrli model (lotin va kirill, `trust_remote_code` bilan yuklanadigan maxsus arxitektura). Kartasida u bilim modeli sifatida mo‘ljallanmagani aytilgan. Litsenziya: Apache-2.0.
- [NeuronAI-Uzbek](https://huggingface.co/NeuronUz/NeuronAI-Uzbek) - O‘zbekcha tokenizatori kengaytirilgan, qo‘shimcha moslashtirilgan Qwen3-4B modeli; kartasida UzLiB baholash natijalari keltirilgan. Litsenziya: Apache-2.0.
- [Qwen3-14B-Base-Uzbek-Cyrillic](https://huggingface.co/Just-Bax/Qwen3-14B-Base-Uzbek-Cyrillic) - Kirill yozuvidagi o‘zbekcha matnga LoRA yordamida moslashtirilgan Qwen3-14B bazaviy modeli (chat uchun emas, matnni davom ettirish uchun). Litsenziya: Apache-2.0.
- [uzbek-gpt-103m](https://huggingface.co/IslombekT/uzbek-gpt-103m) - O‘zining 16 ming birlikli BPE tokenizatori bilan o‘zbek tilida boshidan o‘qitilgan 103 million parametrli kichik dekoder; tadqiqotlar uchun ixcham tayanch model. Litsenziya: Apache-2.0.

### Enkoderlar va seq2seq modellari

- [BERTbek](https://huggingface.co/elmurod1202/bertbek-news-big-cased) - Katta o‘zbekcha yangiliklar korpusida dastlabki o‘qitishdan o‘tgan, katta-kichik harflarni farqlaydigan BERT. Shu muallifning NER, POS, yangiliklar va hissiy munosabat tahlili uchun moslashtirilgan modellari ham bor ([maqola](https://aclanthology.org/2024.sigul-1.5/)). Litsenziya: MIT.
- [t5-base-uzbek](https://huggingface.co/rifkat/t5-base-uzbek) - Matndan matnga vazifalar uchun o‘zbek tilida boshidan o‘qitilgan T5-base. Litsenziya: Apache-2.0.
- [TahrirchiBERT](https://huggingface.co/tahrirchi/tahrirchi-bert-base) - Lotin yozuvidagi o‘zbekcha matnda dastlabki o‘qitishdan o‘tgan, katta-kichik harflarni farqlaydigan 110 million parametrli enkoder; 67 million parametrli [small](https://huggingface.co/tahrirchi/tahrirchi-bert-small) varianti ham bor. Litsenziya: Apache-2.0.
- [UzBERT](https://huggingface.co/coppercitylabs/uzbert-base-uncased) - Kirill yozuvidagi taxminan 625 ming o‘zbekcha yangilik maqolasida dastlabki o‘qitishdan o‘tgan BERT base ([maqola](https://arxiv.org/abs/2108.09814)). Litsenziya: MIT.
- [UzRoBERTa](https://huggingface.co/rifkat/uztext-3Gb-BPE-Roberta) - Lotin va kirill yozuvidagi taxminan 3 GB o‘zbekcha matnda dastlabki o‘qitishdan o‘tgan RoBERTa modeli. Litsenziya: Apache-2.0.
- [XLM-RoBERTa large](https://huggingface.co/FacebookAI/xlm-roberta-large) - Dastlabki o‘qitish ma’lumotlari o‘zbek tilini ham qamrab olgan ko‘p tilli enkoder; o‘zbekcha nomlangan obyektlarni aniqlash va tasniflashda keng qo‘llanadigan tayanch model. Litsenziya: MIT.

### Vektor ifodalar va qidiruv

- [Cross-lingual word embeddings for Turkic languages](https://github.com/elmurod1202/crosLingWordEmbTurk) - O‘zbek, turk, ozarbayjon, qozoq va qirg‘iz tillari uchun o‘zaro moslashtirilgan so‘z vektorlari va ikki tilli lug‘atlar ([LREC 2020 maqolasi](https://aclanthology.org/2020.lrec-1.499/)). Litsenziya ko‘rsatilmagan.
- [fastText word vectors](https://fasttext.cc/docs/en/crawl-vectors.html) - Common Crawl va Vikipediya ma’lumotlarida o‘qitilgan 300 o‘lchamli tayyor o‘zbekcha so‘z vektorlari (`cc.uz.300`). Litsenziya: CC BY-SA 3.0.
- [LaBSE](https://huggingface.co/sentence-transformers/LaBSE) - O‘zbek tilini ham qamrab oladigan, tilga bog‘liq bo‘lmagan gap vektorlarini yaratadi; ko‘pincha ikki tilli parallel matn juftlarini topishda ishlatiladi. Litsenziya: Apache-2.0.
- [ModernUzBERT](https://huggingface.co/Orzumurod/ModernUzBERT) - Semantik qidiruv uchun ModernBERT asosidagi o‘zbekcha gap vektorlari modeli. Litsenziya: Apache-2.0.
- [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large) - Qo‘llaydigan tillari orasida o‘zbek tili ham ko‘rsatilgan umumiy ko‘p tilli matn vektorlari modeli. Litsenziya: MIT.
- [uzbek-e5-small](https://huggingface.co/sukhrobnurali/uzbek-e5-small) - O‘zbekcha semantik qidiruv va o‘zbekcha-inglizcha tillararo qidiruvga moslashtirilgan multilingual-e5-small versiyasi; unga aloqador [uzbek-minilm](https://huggingface.co/sukhrobnurali/uzbek-minilm) modelini ham ko‘ring. Litsenziya: MIT.

### Mashina tarjimasi modellari

- [Dilmash](https://huggingface.co/tahrirchi/dilmash) - Qoraqalpoq, o‘zbek, rus va ingliz tillari o‘rtasida tarjima qiladigan NLLB asosidagi modellar ([maqola](https://arxiv.org/abs/2409.04269)). Litsenziya: CC BY-NC 4.0.
- [Lutfiy](https://huggingface.co/tahrirchi/lutfiy) - Janubiy o‘zbek (arab yozuvi), shimoliy o‘zbek va ingliz tillari uchun NLLB asosidagi tarjima modeli ([maqola](https://arxiv.org/abs/2508.14586)). Litsenziya: CC BY-NC 4.0.
- [MADLAD-400 MT](https://huggingface.co/google/madlad400-3b-mt) - Google yaratgan, o‘zbek tilini ham o‘z ichiga olgan 400 dan ortiq til uchun T5 asosidagi tarjima modellari. Litsenziya: Apache-2.0.
- [NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M) - Meta yaratgan, shimoliy o‘zbek tilini (`uzn_Latn`) ham qamrab olgan 200 tilli tarjima modellari; 1.3B va 3.3B variantlari ham bor. Litsenziya: CC BY-NC 4.0.

### Muayyan vazifalarga mos modellar

- [rubai-corrector-base](https://huggingface.co/islomov/rubai-corrector-base) - ByT5 base asosidagi o‘zbekcha va ruscha matnni tuzatish modeli (tinish belgilari, OCR va avtomatik nutqni tanish xatolari, apostroflarni bir xil shaklga keltirish); alohida vazifalarga mos variantlari bor. Litsenziya ko‘rsatilmagan.
- [UzABSA-LLM](https://huggingface.co/Sanatbek/UzABSA-LLM) - O‘zbekcha matndagi alohida jihatlarga nisbatan hissiy munosabatni tahlil qilish uchun QLoRA bilan moslashtirilgan Qwen 2.5, Llama 3.1 va DeepSeek-R1-Distill modellari. Litsenziya: Apache-2.0.
- [uzbek-ner-xlmr-large](https://huggingface.co/UAzimov/uzbek-ner-xlmr-large) - Uzbek NER Gold to‘plamida o‘zbekcha nomlangan obyektlarni aniqlashga moslashtirilgan XLM-R large. Litsenziya: MIT.
- [uzbek-news-category-classifier](https://huggingface.co/coppercitylabs/uzbek-news-category-classifier) - UzBERT asosida kirill yozuvidagi taxminan 60 ming yangilik maqolasida moslashtirilgan yangilik mavzusi tasniflagichi. Litsenziya: MIT.
- [Uzbek-POS-Tagger-TahrirchiBERT](https://huggingface.co/MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT) - TahrirchiBERT asosida moslashtirilgan so‘z turkumlarini belgilash modeli. Litsenziya: Apache-2.0.

## NLP kutubxonalari va vositalari

- [apertium-uzb](https://github.com/apertium/apertium-uzb) - O‘zbek tili uchun Apertium chekli holatli morfologik o‘zgartirgichi va lingvistik ma’lumotlar. Litsenziya: GPL-3.0.
- [fitrat](https://github.com/tahrirchi/fitrat) - Lotin-kirill transliteratsiyasi (istisnolar ro‘yxatiga ega HFST o‘zgartirgichlari), tilni aniqlash, tokenizatorlar va morfologik tahlilni birlashtirgan Python kutubxonasi. Litsenziya: MIT.
- [Tahrirgoh](https://github.com/tahrirchi/tahrirgoh) - Grammatik xatolarni tuzatish (GEC) ma’lumotlarini yig‘ish uchun veb-platforma. Litsenziya: MIT.
- [Uzbek Hunspell spellchecker](https://uzbek-spell.github.io/) - Hunspell lug‘at fayllari va g‘oyani namoyish qiluvchi MS Office qo‘shimchasi bor tadqiqot imlo tekshirgichi.
- [Uzbek stopwords](https://github.com/elmurod1202/StopWords) - O‘zbek tili uchun avtomatik tuzilgan stop-so‘zlar ro‘yxatlari. Litsenziya: Apache-2.0.
- [uzbek-tagger-bert](https://github.com/MaksudSharipov/uzbek-tagger-bert) - O‘zbekcha so‘z turkumlarini transformerlar asosida belgilash uchun Python kutubxonasi. Litsenziya: Apache-2.0.
- [uzbek-tokenizers](https://github.com/coppercitylabs/uzbek-tokenizers) - O‘zbek tili uchun gap va so‘z tokenizatorlari. Litsenziya ko‘rsatilmagan.
- [uzbek-wordlist](https://github.com/kmashrab/uzbek-wordlist) - Imlo tekshirish lug‘atlarida ishlatiladigan kirill yozuvidagi o‘zbekcha so‘zlar ro‘yxati. Litsenziya: GPL-2.0.
- [UzbekStemmer](https://github.com/MaksudSharipov/UzbekStemmer) - O‘zbekcha so‘z o‘zagini lug‘atsiz, qoidalar asosida ajratuvchi vosita. Litsenziya: MIT uslubidagi litsenziya (repozitoriyga qarang).
- [UzMorphAnalyser](https://github.com/UlugbekSalaev/UzMorphAnalyser) - O‘zbek tili uchun qo‘shimchalarga asoslangan morfologik tahlilchi (o‘zak ajratish, lemmalashtirish, tahlil). Litsenziya: MIT.
- [UzTransliterator](https://github.com/UlugbekSalaev/UzTransliterator) - Qoidalar va statistikani birlashtirib, o‘zbek kirill, amaldagi lotin va taklif etilgan yangi lotin alifbolari o‘rtasida transliteratsiya qiladigan Python paketi. Litsenziya: MIT.
- [UzWordnet](https://github.com/LDKR-Group/UzWordnet) - Princeton WordNet bilan mos o‘zbekcha leksik-semantik ma’lumotlar bazasi ([maqola](https://aclanthology.org/2021.gwc-1.2/)). Litsenziya: CC BY-SA 4.0 (WordNet License shartlari ostidagi Princeton WordNet asosida yaratilgan).

## Ma’lumotlar to‘plamlari

O‘zbekcha modellarni o‘qitish va baholash uchun korpuslar hamda belgilangan ma’lumotlar. Tijoriy foydalanishdan oldin har bir to‘plam kartasidagi shartlarni tekshiring.

### Dastlabki o‘qitish korpuslari

- [CC-100](https://data.statmt.org/cc-100/) - XLM-Rni o‘qitishda ishlatilgan, o‘zbek tilini ham o‘z ichiga olgan bir tilli Common Crawl ma’lumotlari.
- [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) - `uzn_Latn` va `uzn_Cyrl` qismlari bor filtrlangan ko‘p tilli veb-korpus. Litsenziya: ODC-By.
- [HPLT v2 cleaned](https://huggingface.co/datasets/HPLT/HPLT2.0_cleaned) - `uzn_Latn` qismi bor katta ko‘p tilli veb-matn to‘plami. Litsenziya: CC0 (shartlar uchun kartaga qarang).
- [MADLAD-400](https://huggingface.co/datasets/allenai/MADLAD-400) - Hujjat darajasidagi ko‘p tilli Common Crawl korpusi; tozalangan va shovqinli o‘zbekcha qismlari bor. Litsenziya: ODC-By.
- [rubai-text-s60m](https://huggingface.co/datasets/islomov/rubai-text-s60m) - Katta LLMdan distillatsiya orqali yaratilgan, 80 mavzu bo‘yicha taxminan 1,14 million sun’iy o‘zbekcha savol va matn parchasi juftlari. Litsenziya: CC BY 4.0.
- [Uzbek Legal Corpus v1](https://huggingface.co/datasets/sukhrobnurali/uzbek-legal-corpus-v1) - Lex.uzdan olingan O‘zbekiston kodekslari va Konstitutsiyasining moddalar bo‘yicha tuzilgan tadqiqot nusxasi (yuridik maslahat emas). Litsenziya: Apache-2.0.
- [Uzbek Wikipedia dumps](https://dumps.wikimedia.org/uzwiki/) - O‘zbekcha Vikipediya ma’lumotlar bazasining rasmiy Wikimedia eksportlari. Litsenziya: CC BY-SA.
- [UzBooks v2](https://huggingface.co/datasets/tahrirchi/uz-books-v2) - OCR orqali matnga aylantirilgan qariyb 40 ming o‘zbekcha kitob; lotin va kirillga transliteratsiya qilingan qismlar shaklida berilgan. Litsenziya: MIT.
- [UzCrawl](https://huggingface.co/datasets/tahrirchi/uz-crawl) - Taxminan 1,2 million veb va Telegram manbasidan yig‘ilgan o‘zbekcha korpus (v2 2024-yil martigacha yangilangan). Litsenziya: Apache-2.0.

### Ko‘rsatmalar va afzalliklar ma’lumotlari

- [alpaca-cleaned-uz](https://huggingface.co/datasets/behbudiy/alpaca-cleaned-uz) - Google Translate yordamida o‘zbekchaga mashina tarjimasi qilingan Alpaca-cleaned ko‘rsatmalari. Litsenziya ko‘rsatilmagan.
- [DPO-uz-9k](https://huggingface.co/datasets/MLDataScientist/DPO-uz-9k) - DPO usulida o‘qitish uchun o‘zbekchaga mashina tarjimasi qilingan taxminan 9 ming afzal va afzal bo‘lmagan javob jufti. Litsenziya: Apache-2.0.
- [oasst2_uzbek](https://huggingface.co/datasets/MLDataScientist/oasst2_uzbek) - NLLB-200 3.3B yordamida o‘zbekchaga mashina tarjimasi qilingan OpenAssistant OASST2 suhbatlari. Litsenziya: Apache-2.0.
- [translation-instruction](https://huggingface.co/datasets/behbudiy/translation-instruction) - Inglizcha-o‘zbekcha tarjima va tillararo ko‘rsatmalarning 20 ming namunasi. Litsenziya ko‘rsatilmagan.
- [uzbek-instruct-llm](https://huggingface.co/datasets/UAzimov/uzbek-instruct-llm) - Asosan mavjud ko‘rsatmalar to‘plamlaridan tarjima qilingan 15 mingdan ortiq o‘zbekcha ko‘rsatma yozuvi. Litsenziya: Apache-2.0.

### Muayyan vazifalar uchun to‘plamlar

- [Dilmash corpus](https://huggingface.co/datasets/tahrirchi/dilmash) - Qoraqalpoq tilini o‘zbek, rus va ingliz tillari bilan juftlaydigan parallel korpuslar. Litsenziya: MIT.
- [Lutfiy corpus](https://huggingface.co/datasets/tahrirchi/lutfiy) - Janubiy o‘zbek tili bilan shimoliy o‘zbek yoki ingliz tili o‘rtasidagi taxminan 40 ming parallel gap. Litsenziya: MIT.
- [rubai-NER-150K-Personal](https://huggingface.co/datasets/islomov/rubai-NER-150K-Personal) - Shaxsni aniqlashga oid ma’lumotlarni (PII) topish uchun o‘zbek va rus tillaridagi 142 704 ta sun’iy namuna. Litsenziya: Apache-2.0.
- [SimRelUz](https://huggingface.co/datasets/elmurod1202/SimRelUz_semantic_evaluation_dataset) - O‘xshashligi va ma’noviy aloqadorligi odamlar tomonidan baholangan mingdan ortiq o‘zbekcha so‘z jufti ([maqola](https://aclanthology.org/2022.sigul-1.26/)). Litsenziya ko‘rsatilmagan.
- [UD Uzbek-UT](https://universaldependencies.org/treebanks/uz_ut/index.html) - O‘zbek tili uchun birinchi Universal Dependencies sintaktik daraxtlar korpusi (yangiliklar va badiiy asarlardan 500 ta gap); [UzUDT](https://universaldependencies.org/treebanks/uz_uzudt/index.html) va [TueCL](https://universaldependencies.org/treebanks/uz_tuecl/index.html)ni ham ko‘ring. Litsenziya: CC BY-SA 4.0.
- [Uzbek ABSA](https://huggingface.co/datasets/Sanatbek/aspect-based-sentiment-analysis-uzbek) - SemEval-2014 formatidagi o‘zbekcha sharhlarda alohida jihatlarga nisbatan hissiy munosabatni tahlil qilish to‘plami. Litsenziya ko‘rsatilmagan.
- [Uzbek NER Gold](https://huggingface.co/datasets/uznlp-uz/uzbek_NER) - Shaxs, tashkilot, joy, pul, sana va boshqa obyekt turlari BIO belgilari bilan ko‘rsatilgan 4 176 ta gap. Litsenziya: CC BY 4.0.
- [Uzbek sentiment analysis](https://github.com/elmurod1202/uzbek-sentiment-analysis) - Birinchi belgilangan o‘zbekcha hissiy munosabat tahlili to‘plami (ilova sharhlari); tayanch model kodi ham bor. Litsenziya ko‘rsatilmagan.
- [Uzbek text classification dataset](https://huggingface.co/datasets/murodbek/uz-text-classification) - 9 ta saytdan olingan, 15 toifaga ajratilgan lotin yozuvidagi 512 750 ta yangilik maqolasi ([maqola](https://arxiv.org/abs/2302.14494)). Litsenziya ko‘rsatilmagan.
- [Uzbek zero-shot classification](https://huggingface.co/datasets/risqaliyevds/uzbek-zero-shot-classification) - 10 ta mavzu toifasi bilan belgilangan o‘zbekcha yangilik matnlari. Litsenziya: MIT.
- [uzbek-embedding-pairs](https://huggingface.co/datasets/sukhrobnurali/uzbek-embedding-pairs) - Vektor ifoda modellarini o‘qitish uchun 356 ming parallel va bir tilli o‘zbekcha gap jufti. Litsenziya: Apache-2.0.
- [Uzbek-Kazakh parallel corpus](https://huggingface.co/datasets/Sanatbek/uzbek-kazakh-parallel-corpora) - O‘zbekcha-qozoqcha mashina tarjimasi uchun parallel gaplar. Litsenziya ko‘rsatilmagan.
- [uzbek_ner](https://huggingface.co/datasets/risqaliyevds/uzbek_ner) - Shaxs, joy, tashkilot, sana va boshqa obyekt turlari bor JSON formatidagi nomlangan obyektlarni aniqlash to‘plami. Litsenziya: MIT.
- [UzbekLemmaStems-POS-Dataset](https://github.com/MaksudSharipov/UzbekLemmaStems-POS-Dataset) - Morfologiya tadqiqotlari uchun o‘zbekcha so‘zlarning lemma va o‘zaklari so‘z turkumi belgilari bilan berilgan to‘plam. Litsenziya: Apache-2.0.
- [UzbekPOS](https://huggingface.co/datasets/latofat/uzbekpos) - BBPOS ishidan olingan, UPOS bo‘yicha belgilangan birinchi o‘zbekcha to‘plam (lotin va kirill yozuvidagi 250 ta gap; [maqola](https://arxiv.org/abs/2501.10107)). Litsenziya: Apache-2.0.

### Nutq ma’lumotlari to‘plamlari

- [FeruzaSpeech](https://arxiv.org/abs/2410.00035) - Tinish belgilari, katta-kichik harflar va kontekst saqlangan 60 soatlik o‘zbekcha o‘qib berilgan nutq korpusi (2024). Foydalanish shartlari uchun maqolaga qarang.
- [USC: Uzbek Speech Corpus](https://arxiv.org/abs/2107.14419) - 958 nafar so‘zlovchidan olingan 105 soatlik ochiq o‘zbekcha nutqni tanish korpusi va tayanch tajribalar (2021). Foydalanish shartlari uchun maqolaga qarang.
- [UzbekVoice dataset project](https://discourse.mozilla.org/t/creating-open-and-accessible-resources-for-uzbek-the-uzbekvoice-ai-project/112634) - UzbekVoiceAI ortidagi jamoaning ochiq o‘zbekcha matn va ovoz to‘plami loyihasi haqida Mozilla Discourse forumidagi ma’lumot (taxminan 1 400 soat yig‘ilgan).

## Baholash to‘plamlari

- [Belebele](https://huggingface.co/datasets/facebook/belebele) - `uzn_Latn` qismi bor ko‘p tilli o‘qib tushunishni baholash to‘plami. Litsenziya: CC BY-SA 4.0.
- [FLORES+](https://huggingface.co/datasets/openlanguagedata/flores_plus) - Shimoliy (`uzn_Latn`) va janubiy (`uzs_Arab`) o‘zbek tillarini qamrab olgan mashina tarjimasini baholash to‘plami; foydalanish uchun Hugging Face shartlarini qabul qilish talab etiladi. Litsenziya: CC BY-SA 4.0.
- [Global PIQA](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-nonparallel) - O‘zbekcha qismi bor, madaniy xususiyatlarni hisobga oluvchi kundalik jismoniy vaziyatlarni tushunish va mantiqiy baholash to‘plami. Litsenziya: CC BY-SA 4.0.
- [IdrockBench](https://github.com/idrock-ai/IdrockBench) - Yangi O‘zbekiston universitetining IDROCK AI Excellence Center markazi yaratgan o‘zbekcha LLMlarni baholash to‘plami (imtihonlarga asoslangan bilim, mulohaza yuritish, ko‘rsatmalarga amal qilish, tarjima). Litsenziya: MIT.
- [INCLUDE](https://huggingface.co/datasets/CohereLabs/include-base-44) - O‘zbekcha qismi bor, hududga xos bilimlarni imtihon savollari orqali tekshiradigan ko‘p tilli baholash to‘plami. Litsenziya: Apache-2.0.
- [Kardeş-NLU](https://github.com/lksenel/Kardes-NLU) - O‘zbek tilini ham o‘z ichiga olgan besh turkiy til uchun tabiiy tilni tushunishni baholash to‘plami ([EACL 2024 maqolasi](https://aclanthology.org/2024.eacl-long.100/)). Litsenziya ko‘rsatilmagan.
- [MMLU-uz](https://huggingface.co/datasets/murodbek/MMLU-uz) - Mashina tarjimasi qilingan va inson tekshiruvidan o‘tmagan o‘zbekcha MMLU; [Lite](https://huggingface.co/datasets/murodbek/MMLU-Lite-uz) versiyasi ham bor. Litsenziya: Apache-2.0.
- [SIB-200](https://huggingface.co/datasets/Davlan/sib200) - FLORES-200 asosidagi mavzu tasnifini baholash to‘plami; `uzn_Latn`ni ham o‘z ichiga oladi. Litsenziya: CC BY-SA 4.0.
- [TUMLU](https://github.com/ceferisbarov/TUMLU) - O‘zbek tilini ham o‘z ichiga olgan turkiy tillarda bevosita tuzilgan (tarjima qilinmagan) maktab darajasidagi bilimlarni baholash to‘plami; [TUMLU-mini](https://huggingface.co/datasets/jafarisbarov/TUMLU-mini) Hugging Faceda mavjud ([maqola](https://arxiv.org/abs/2502.11020)). Litsenziya: CC BY 4.0 (ma’lumotlar to‘plami).
- [UzLiB](https://github.com/tahrirchi/uzlib) - Uzbek Linguistic Benchmark: o‘zbekcha to‘g‘ri yozish, so‘z qo‘llash va ma’noga oid variantli savollar; baholash kodi va ochiq natijalar reytingi mavjud ([to‘plam](https://huggingface.co/datasets/tahrirchi/uzlib)). Litsenziya: MIT.
- [WikiANN](https://huggingface.co/datasets/unimelb-nlp/wikiann) - O‘zbekcha qismi bor, avtomatik belgilangan («silver») ko‘p tilli nomlangan obyektlarni aniqlash ma’lumotlari. Litsenziya ko‘rsatilmagan.
- [XL-Sum](https://huggingface.co/datasets/csebuetnlp/xlsum) - O‘zbekcha qismi bor BBC maqolalari asosidagi, matn mazmunini qayta ifodalab qisqartirish to‘plami. Litsenziya: CC BY-NC-SA 4.0.

## Ta’lim

O‘zbek tilida AIni o‘rganish manbalari. Pullik manbalar alohida belgilangan.

### Kurslar va platformalar

- [AiStudy.uz](https://aistudy.uz/) - Raqamli texnologiyalar vazirligining o‘zbek tilida AI asoslarini o‘rgatuvchi bepul milliy onlayn platformasi, AI Leaders milliy dasturining bir qismi. Unga aloqador [omp.aistudy.uz](https://omp.aistudy.uz/) sayti keng jamoatchilikka prompt yozishni o‘rgatadi.
- [Besh million sun’iy intellekt yetakchilari](https://aileaders.uz/) - Raqamli ta’limni rivojlantirish markazi yuritadigan bepul milliy onlayn ta’lim platformasi (AI Leaders), «One Million Uzbek Coders» dasturining davomi (uzbekcoders.uz hozir shu saytga yo‘naltiradi). O‘zbekcha interfeys hamda Coursera va Alison kabi hamkorlarning AI, ma’lumotlar va IT kurslari bor; kurslarning tili turlicha. Rasmiy Telegram: [@aileaders_uz](https://t.me/aileaders_uz).
- [Mohirdev](https://mohirdev.uz/) - O‘zbek tilidagi onlayn IT maktabi. Kurslari orasida olti oylik [Data sayns va sun’iy intellekt](https://mohirdev.uz/kasblar/data-science-va-suniy-intellekt/) dasturi (Python, ML, chuqur o‘rganish, NLP) va qisqaroq [NLP kursi](https://mohirdev.uz/kasblar/nlp/) bor. Telegram: [@mohirdev](https://t.me/mohirdev). Pullik.
- [Xarita.ai](https://xarita.ai/) - Hamjamiyat yaratgan, AIni o‘rganish uchun o‘zbekcha bepul yo‘l xaritalari. Dasturchilar va oddiy foydalanuvchilar uchun alohida yo‘nalishlar, bepul kurslar va kitoblarga havolalar bor. Google Developer Expert Adkham Zokhirov 2026-yilda boshlagan.
- [Yandex ML School Uzbekistan](https://mlschool.yandex.uz/) - Yangi O‘zbekiston universiteti bilan hamkorlikda Toshkentda o‘tkaziladigan bepul, tanlov asosidagi bir yillik mashinaviy o‘rganish dasturi. Kechki yuzma-yuz darslar ingliz tilida; qabul onlayn test, imtihon va suhbat orqali amalga oshiriladi.

### O‘zbekcha qo‘llanmalar

- [ChatGPT talabalar uchun: 20 usul va promptlar](https://gptbot.uz/uz/blog/chatgpt-talabalar-uchun/) - AI-chat yordamida o‘qish bo‘yicha o‘zbekcha qo‘llanma (mavzuni tushuntirish, qaydlar, test mashqlari, tarjima, faktlarni tekshirish), akademik halollik qoidalari bilan. Usullar faqat ChatGPTda emas, istalgan AI-chatda ishlaydi. Manfaatdorlik haqida: GPTBot.uz jamoasi yuritadi; GPTBot.uz mustaqil xizmat bo‘lib, OpenAI bilan bog‘liq emas.
- [ChatGPT uchun o‘zbek tilida 50 ta tayyor prompt](https://gptbot.uz/uz/blog/chatgpt-uzbek-tilida-promptlar/) - O‘qish, ish, marketing, savdo va kundalik vazifalar uchun moslashtirishga tayyor 50 ta o‘zbekcha prompt; istalgan AI-chatda ishlaydi. Manfaatdorlik haqida: GPTBot.uz jamoasi yuritadi.
- [Neyrotarmoqlar uchun promptlar: ChatGPT va boshqa neyron tarmoqlar](https://mohirdev.uz/blog/neyrotarmoqlar-uchun-promptlar-chatgpt-va-boshqa-neyron-tarmoqlarga-sorovlarni-qanday-yozish-kerak/) - Mohirdevning ChatGPT va rasm hamda video generatorlari (Midjourney, Stable Diffusion, Shedevrum, Kandinsky) uchun prompt yozish haqidagi batafsil o‘zbekcha qo‘llanmasi (2024), amaliy misollar bilan.
- [O‘qituvchilar uchun 12 ta sun’iy intellekt vositasi](https://abt.uz/blog/oqituvchilar-uchun-talimni-yaxshilovchi-12-ta-eng-samarali-suniy-intellekt-vositasi) - abt.uzda chop etilgan, dars rejalash va sinfdagi ishlar uchun 12 ta AI vositasi haqidagi o‘qituvchilarga mo‘ljallangan o‘zbekcha maqola.
- [O‘qituvchilar uchun ChatGPT](https://mohirdev.uz/blog/Oqituvchilar-uchun-ChatGPT/) - Maktab o‘qituvchilari uchun dars rejalari, topshiriqlar va baholashda ChatGPT yordamida vaqt tejash haqidagi Mohirdev maqolasi (2025); o‘zbekcha prompt namunalari bor.
- [Prompt engineering: TOP tavsiyalar](https://mohirdev.uz/blog/Prompt-Engineering-nega-kerak/) - Mohirdevning prompt engineering nima ekani va nima uchun muhimligini tushuntiruvchi maqolasi (2025). AI modellari bilan muloqot qilish va ulardan dasturlashda foydalanishning amaliy usullarini beradi; Googlening prompt engineering bo‘yicha texnik qo‘llanmasiga tayanadi.
- [Sun’iy intellekt (O‘zbekcha Vikipediya)](https://uz.wikipedia.org/wiki/Sun%CA%BCiy_intellekt) - O‘zbekcha Vikipediyadagi AI haqidagi umumiy maqola; batafsilroq [Generativ sun’iy intellekt](https://uz.wikipedia.org/wiki/Generativ_sun%CA%BCiy_intellekt) maqolasi generativ modellarni yoritadi. Ikkalasini ham istalgan kishi yaxshilashi mumkin.

### Videodarslar

- [Adkham Zokhirov](https://www.youtube.com/@zokhirov) - Mashinaviy o‘rganish bo‘yicha Google Developer Expertning asosan o‘zbek tilidagi AI va ML darslari, o‘quv yo‘l xaritalari va kasbiy maslahatlari. Telegram: [@adkham_zokhirov](https://t.me/adkham_zokhirov).
- [Machine Learning fanini o‘rganish (Machine Learning Lab)](https://www.youtube.com/playlist?list=PLm6Oe3KKPuWHdt2FxDJ3JSUF2LCalYSze) - O‘zbek tilidagi tizimli mashinaviy o‘rganish kursi (nazoratli va nazoratsiz o‘rganish, chiziqli regressiya, xarajat funksiyasi, gradient tushish usuli, kod yozish mashg‘ulotlari), 2022–2023-yillar; kanalda NumPy turkumi ham bor.
- [Mohirdev on YouTube](https://www.youtube.com/@Mohirdev) - Data science va AI kurslari uchun bepul kirish videolari, AI vositalaridan foydalanish darslari, uchrashuvlar va intervyular beriladigan o‘zbekcha IT-ta’lim kanali.
- [Sariq dev](https://www.youtube.com/@Sariqdev) - Mohirdev asoschisi Anvar Narzullaev kanali; Data Science pleylisti, AI haqida tushuntirishlar va haftalik o‘zbekcha AI yangiliklari dasturi bor. Telegram: [@sariqdev](https://t.me/sariqdev).
- [Sun’iy intellekt (Milliy ta’lim resurslari)](https://www.youtube.com/playlist?list=PLFRnhpV9odGBNt4Xm_dRcgsPeI9pPwzeK) - Maktabgacha va maktab ta’limi vazirligi tayyorlagan materiallarni e’lon qiladigan kanaldagi maktab darajasiga mos 21 ta o‘zbekcha dars (AI tarixi, ahamiyati, neyron tarmoqlar, evolyutsion usullar, sensorlar).
- [Sun’iy intellekt va PyTorch (AMDUz)](https://www.youtube.com/playlist?list=PLqWThajMX99UDVYl2_W2a7pTdmDfFSq9M) - Python va PyTorch yordamida mashinaviy hamda chuqur o‘rganish asoslari bo‘yicha 12 ta o‘zbekcha dars (2020–2021).

### Ilmiy maqolalar

- [Cloud and On-Premises Deployment of Uzbek Legal RAG](https://arxiv.org/abs/2608.29284) - O‘zbek tilidagi, qidirib topilgan ma’lumot bilan javobini boyitadigan yuridik savol-javob yordamchisini bulutda va tashkilotning o‘z infratuzilmasida ishga tushirish tajribalari (2026).
- [Creating a morphological and syntactic tagged corpus for the Uzbek language](https://arxiv.org/abs/2210.15234) - Belgilangan o‘zbekcha korpus yaratish uchun so‘z turkumlari va sintaktik belgilar tizimi (2022).
- [Development of Word Embeddings for Uzbek Language](https://arxiv.org/abs/2009.14384) - Kirill yozuvidagi o‘zbek tili uchun ommaga taqdim etilgan birinchi word2vec, GloVe va fastText vektorlari (2020).
- [Recent Advancements and Challenges of Turkic Central Asian Language Processing](https://arxiv.org/abs/2407.05006) - O‘zbek, qozoq, qirg‘iz va turkman tillari uchun NLP resurslari va usullari sharhi (2024).
- [Uzbek Cyrillic-Latin-Cyrillic Machine Transliteration](https://arxiv.org/abs/2101.05162) - Ikki o‘zbek yozuvi o‘rtasida ma’lumotlarga asoslangan transliteratsiya (2021).
- [Uzbek Sentiment Analysis based on local Restaurant Reviews](https://arxiv.org/abs/2205.15930) - Restoran sharhlaridagi hissiy munosabatni tahlil qilish to‘plami va tayanch modellar (2022).
- [UzbekTagger: The rule-based POS tagger for Uzbek language](https://arxiv.org/abs/2301.12711) - 20 soha bo‘yicha muvozanatlangan, 12 turdagi so‘z turkumi belgisi qo‘yilgan to‘plam va qoidalarga asoslangan belgilash vositasi (2023).

## Hamjamiyat

O‘zbekistonda va o‘zbek tili uchun AI yaratayotgan odamlar hamda tashkilotlar.

### Hamjamiyatlar va Telegram kanallari

- [AICA](https://aica.uz/) - Toshkentdagi Markaziy Osiyo sun’iy intellekt assotsiatsiyasi. AICA Awards va ta’lim dasturlarini o‘tkazadi, Milliy AI Hackathonni hamkorlikda tashkil qiladi.
- [Data Community Uz](https://t.me/datacommunityuz) - Muntazam yuzma-yuz uchrashuvlar o‘tkazadigan Toshkentdagi ma’lumotlar muhandislari, tahlilchilar va ML mutaxassislari hamjamiyati; yozuvlar asosan rus tilida.
- [Databek](https://t.me/databek) - [Hugging Face](https://huggingface.co/databek)da o‘zbekcha ma’lumotlar to‘plamlarini e’lon qiladigan va ma’lumotlar muhandisligi dasturlarini ulashadigan kichik ochiq ma’lumotlar va AI hamjamiyati.
- [GDG Tashkent](https://gdg.community.dev/gdg-tashkent/) - 13 mingdan ortiq a’zosi bor mustaqil Google Developer Group; bepul Build with AI uchrashuvlari, g‘oya tanlovlari, hakatonlar va DevFestni o‘tkazadi. Telegram: [@gdgtashkent](https://t.me/gdgtashkent).
- [Global AI Tashkent](https://globalai.community/chapters/tashkent) - Markaziy Osiyodagi birinchi Global AI Community bo‘limi. Raqamli texnologiyalar vazirligi huzuridagi Sun’iy intellekt va raqamli iqtisodiyotni rivojlantirish markazi mezbonlik qiladi; muntazam ma’ruzalar va tadbirlar o‘tkaziladi.
- [ML Community Uzbekistan](https://mlcommunity.uz/) - 2021-yilda Toshkentdagi Inha universitetida boshlangan AI hamjamiyati. Uchrashuvlar, ta’lim dasturlari va hakatonlar o‘tkazadi, Milliy AI Hackathonni hamkorlikda tashkil qiladi. Telegram: [@mlc_uz](https://t.me/mlc_uz).

### Tadbirlar va tanlovlar

- [AI Tinkerers Tashkent](https://tashkent.aitinkerers.org/) - AI yaratuvchilarining global uchrashuvlari tarmog‘ining Toshkent bo‘limi; savdo taqdimotlari o‘rniga jonli namoyishlar va texnik ma’ruzalar o‘tkaziladi.
- [ICTWEEK Uzbekistan](https://www.ictweek.uz/eng) - Toshkentdagi yillik milliy AKT haftaligi; 2026-yil dasturiga AI etikasi forumi va Future Intelligence Forum kiritilgan.
- [International Olympiad in Artificial Intelligence (IOAI)](https://ioai-official.org/) - O‘rta maktab o‘quvchilari uchun AI olimpiadasi. O‘zbekiston 2025-yil dekabrida uni g‘oliblari davlat rag‘batiga ega bo‘ladigan xalqaro olimpiadalar ro‘yxatiga qo‘shgan (hukumatning 797-son qarori).
- [National AI Hackathon](https://www.it-park.uz/en/itpark/news/samarqandda-ikkinchi-milliy-ai-hackathon-bo-lib-o-tadi) - Raqamli texnologiyalar vazirligi, IT Park va hamkorlar 2025-yil oktabridan buyon o‘tkazayotgan respublika bo‘ylab hududiy AI hakatonlari turkumi (sog‘liqni saqlash, ta’lim, tadbirkorlik va boshqa yo‘nalishlar). Final 2026-yil dekabrida Toshkentda rejalashtirilgan.
- [President AI Award](https://awards.gov.uz/en/paia) - O‘zbekistondagi AI startaplari uchun milliy tanlov (ishlaydigan prototipga ega 3–8 kishilik jamoalar). G‘oliblar investitsiya oladi, ariza topshirish bepul.

### Davlat dasturlari

- [AI Development Strategy until 2030](https://lex.uz/docs/7159258) - Milliy AI strategiyasi, 2024–2026-yillar chora-tadbirlar rejasi va yaratiladigan ma’lumotlar to‘plamlari ro‘yxatini o‘z ichiga olgan Prezidentning 2024-yil 14-oktabrdagi PQ-358-son qarori. Lex.uzda o‘zbek va rus tillaridagi rasmiy matn hamda norasmiy inglizcha tarjima berilgan.
- [AI O‘zbekiston](https://ai.gov.uz/ai/uz) - Yangiliklar, tadqiqotlar, ta’lim va davlat AI loyihalari bo‘limlari bor milliy AI portali (ai.gov.uz); ayrim bo‘limlar hali to‘ldirilmoqda.
- [IT Park Uzbekistan](https://www.it-park.uz/) - Rezidentlik, startap va ta’lim dasturlarini yuritadigan, milliy AI hakatonlari va tadbirlarini hamkorlikda tashkil qiladigan davlat texnologiyalar parki.
- [Sun’iy intellekt (Ministry of Digital Technologies)](https://gov.uz/oz/digital/activity_page/sun-iy-intellekt) - Vazirlikning AI siyosati, 2030-yilgacha strategiya, tegishli huquqiy hujjatlar va AI yangiliklari haqidagi sahifasi.

### Tadqiqot guruhlari

- [Behbudiy Labs](https://huggingface.co/behbudiy) - O‘zbek tiliga moslashtirilgan Llama va Mistral ko‘rsatma modellari, o‘zbekcha ko‘rsatmalar, tarjima va hissiy munosabat tahlili to‘plamlarini e’lon qiladi.
- [Elmurod Kuriyozov](https://github.com/elmurod1202) - Urganch davlat universitetidagi o‘zbekcha NLP tadqiqotchisi. Repozitoriylari hissiy munosabat tahlili to‘plamlari, stop-so‘zlar, tillararo so‘z vektorlari va boshqa o‘zbekcha resurslarni qamrab oladi.
- [IDROCK AI Lab](https://github.com/idrock-ai) - Yangi O‘zbekiston universitetining AI laboratoriyasi. O‘zbekcha til modellarini baholash uchun IdrockBench hamda O‘zbekistondagi oliygohga kirish imtihoni asosidagi baholash to‘plamida promptlarni optimallashtirish tadqiqotini e’lon qiladi.
- [ISSAI](https://issai.nu.edu.kz/) - Nazarboyev universitetidagi (Qozog‘iston) Aqlli tizimlar va sun’iy intellekt instituti. O‘zbekistonlik hamkorlar bilan ochiq Uzbek Speech Corpusni chiqargan va turkiy tillarning nutq hamda til texnologiyalari ustida ishlaydi.
- [SIGTURK](https://sigturk.github.io/) - ACLning turkiy tillar bo‘yicha maxsus qiziqish guruhi. Uning ilmiy seminarlari ([2024-yil materiallari](https://aclanthology.org/events/sigturk-2024/), [2026-yil materiallari](https://aclanthology.org/events/sigturk-2026/)) turkiy tillar NLPsi uchun asosiy maydon hisoblanadi. 2026-yil to‘plamiga o‘zbek tilini ham qamrab olgan besh turkiy tildagi iboralarni baholash to‘plami kiritilgan.
- [Tahrirchi](https://huggingface.co/tahrirchi) - O‘zbek va turkiy tillar NLPsi (grammatikani tuzatish, tarjima) ustida ishlaydigan Toshkent jamoasi. TahrirchiBERT, UzLiB baholash to‘plami va Dilmash tarjima modellarini chiqargan.
- [Uzbek LLM Lab](https://huggingface.co/uzlm) - Ochiq LLMlarni o‘zbek tiliga moslashtiradigan guruh (alloma 1B–8B modellari); o‘zbekcha matnni nutqqa aylantirish modelini ham chiqargan.

### Ochiq ma’lumot loyihalari

- [Common Voice: Uzbek](https://commonvoice.mozilla.org/uz) - Mozilla ochiq nutq to‘plami uchun o‘zbekcha gaplarni o‘qib yozib oling yoki boshqalarning yozuvlarini tekshiring; texnik ko‘nikmalar talab etilmaydi.

## Aloqador ro‘yxatlar

- [Awesome Uzbek NLP](https://github.com/Abdusalom0v/awesome-uzbek-nlp) - O‘zbekcha NLP ma’lumotlar to‘plamlari, modellar, vositalar va ilmiy maqolalar jamlangan yana bir ro‘yxat.

## Hissa qo‘shish

Takliflar, jumladan ro‘yxatdagi xizmatlarning raqobatchilari ham qabul qilinadi. Issue yoki pull request ochishdan oldin [hissa qo‘shish qoidalari](CONTRIBUTING.md) bilan tanishing.
