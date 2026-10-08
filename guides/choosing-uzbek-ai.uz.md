# O‘zbek tili uchun AI tanlash: amaliy qo‘llanma

[English](choosing-uzbek-ai.md) · [Resurslar ro‘yxati](../README.uz.md) · [Baholash to‘plami](../evaluations/README.md)

Avval natijasini tekshira oladigan vazifani tanlang. O‘zbekcha ravon javob yozadigan servis ham ismni noto‘g‘ri tushunishi, sonni o‘zgartirishi yoki mavjud bo‘lmagan manbani keltirishi mumkin. Ushbu qo‘llanma mos vositalarni tanlash va qaroringizni dalillar bilan asoslashga yordam beradi. Unda mahsulotlar reytingi yoki amalda o‘lchangan taqqoslash natijalari yo‘q.

## 1. Maqsadingizga mos yo‘lni tanlang

- **AIdan hozir foydalanish:** [ilovalar va xizmatlar](../README.uz.md#ilovalar-va-xizmatlar) bo‘limidan boshlang. Matn qoralamasi va tushuntirishlar uchun chat yordamchilarini, tarjima uchun tarjimonlarni, audio va skanlar uchun esa nutq hamda OCR vositalarini solishtiring. Chatga obuna API orqali foydalanishni ham o‘z ichiga oladi, deb hisoblamang.
- **Ilova yaratish:** [til modellari](../README.uz.md#til-modellari) va [NLP vositalarini](../README.uz.md#nlp-kutubxonalari-va-vositalari) ko‘rib chiqing. Tayyor API kerakmi yoki modelni o‘z qurilmangizda ishlatasizmi, aniqlang. Integratsiya imkoniyati va litsenziyani loyihani boshlashdan oldin tekshiring. Telegram loyihasi uchun [ishga tushirish ro‘yxatidan](telegram-bot-checklist.uz.md) foydalaning.
- **Ma’lumot topish yoki modelni baholash:** [ma’lumotlar to‘plamlari](../README.uz.md#malumotlar-toplamlari) va [benchmarklar](../README.uz.md#baholash-toplamlari) bo‘limlariga qarang. Vazifa, yozuv, manba, litsenziya hamda o‘qitish va sinov qismlarining ajratilishini tekshiring. Tarjima qilingan to‘plam bilan dastlab o‘zbekcha yaratilgan to‘plam bir xil jihatlarni tekshirmaydi.
- **O‘rganish:** [kurslar va ta’lim platformalari](../README.uz.md#kurslar-va-platformalar) bo‘limidan boshlang. Matnni toifalarga ajratish yoki hujjatlar ichidan qidirish prototipi kabi kichik maqsad tanlang. Uni yakunlash uchun kerak bo‘lgan vositalarni bosqichma-bosqich o‘rganing.

## 2. Vazifani qisqacha yozib chiqing

Vositalarni solishtirishdan oldin quyidagilarni aniqlang:

- **Kirish ma’lumoti:** matn, skanerlangan sahifa, audio yoki tuzilgan ma’lumot; odatiy hajm va fayl formati.
- **Natija:** aynan nima tayyor bo‘lishi kerak, uni kim o‘qiydi va qayerda ishlatadi.
- **Til:** o‘zbek lotin yozuvi, kirill yozuvi, o‘zbekcha-ruscha aralash matn yoki boshqa zarur tillar. Hududiy so‘zlar va ismlarni ham hisobga oling.
- **Sifat:** sana, summa, ism, iqtibos yoki manba havolasi kabi qaysi qismlar o‘zgarmasligi kerak.
- **Maxfiylik:** qaysi ma’lumot qurilmangiz yoki tashkilotingizdan tashqariga chiqishi mumkin, bunga kim ruxsat beradi va u qancha vaqt saqlanadi.
- **Ish jarayoni:** kutiladigan foydalanish hajmi, maqbul kutish vaqti, xarajat chegarasi va xatolar uchun mas’ul shaxs.

Masalan, odam tekshirib yuboradigan savol-javob qoralamasi bilan CRMdagi buyurtmani o‘zgartiradigan yordamchiga qo‘yiladigan talablar farq qiladi. Vazifa tavsifida bu ikki ishni alohida ko‘rsating.

## 3. Bir nechta variantni bir xil sharoitda solishtiring

Kerakli bo‘limdan ikki yoki uchta variant tanlang. Har biriga bir xil ma’lumot, topshiriq va natija formatini bering. Sana, mavjud bo‘lsa mahsulot yoki model versiyasi, sozlamalar va internetdan qidirish kabi qo‘shimcha vositalar yoqilganini qayd eting. Ishlatmoqchi bo‘lgan usulingizni sinang: saytdagi javob API yoki mahalliy model ham xuddi shunday ishlashini isbotlamaydi.

Har bir variantning asl javobini saqlang va quyidagilarni tekshiring:

- **Ma’no:** topshiriq, ismlar, sonlar va noaniqliklar saqlanganmi?
- **O‘zbekcha matn sifati:** jumlalar tabiiy tuzilganmi, so‘ralgan yozuvga rioya qilinganmi, tutuq va o‘/g‘ belgilari hamda qo‘shimchalar to‘g‘rimi?
- **Vazifaning bajarilishi:** javob kerakli formatdami, uni qayta tuzmasdan ishlatsa bo‘ladimi?
- **Dalillar:** keltirilgan sahifalar mavjudmi va da’volarni tasdiqlaydimi? Ishonchli ko‘ringan havolaning o‘zi yetarli emas.
- **Ma’lumot yetishmagandagi javob:** vosita aniqlashtiruvchi savol beradimi yoki cheklovini aytadimi? Yo‘q ma’lumotni to‘qimaydimi?
- **Mehnat va xarajat:** aynan shu vazifa uchun qancha tekshirish, tahrir, kutish va pullik foydalanish talab qilindi?

Muhim ommaviy matnni o‘zbek tilini yaxshi biladigan kishiga tekshirtiring. Imlo vositalari yordam beradi, lekin ular faktlarning to‘g‘riligini kafolatlamaydi. Qisqa sinov dastlabki tanlov uchun xizmat qiladi; u umumiy benchmark ham, ishonchlilik isboti ham emas.

## 4. Kichik til sinovlarini o‘tkazing

Quyidagi misollar ataylab tuzilgan. Ular haqiqiy mijozlar yozishmalari yoki o‘lchangan sinov natijalari emas. Maxfiy ma’lumotlarni olib tashlagach, o‘z vazifangizga xos misollarni ham qo‘shing. Takrorlash mumkin bo‘lgan taqqoslash uchun [baholash to‘plamidan](../evaluations/README.md) foydalaning.

### Tahrir paytida faktlarni saqlash

So‘rov: “Quyidagi xabarni mijozga mos, muloyim o‘zbekcha matnga aylantiring. Sana, vaqt va ismni o‘zgartirmang. Yangi va’da qo‘shmang: Dilnoza, uchrashuv 12-noyabr kuni soat 15:30 da. Hujjatlar hali tasdiqlanmadi.”

Javobda Dilnoza, 12-noyabr va 15:30 saqlanganini tekshiring. Hujjatlar tasdiqlangan, deb yozilmasligi kerak. Ohang muloyim bo‘lsin, lekin ortiqcha rasmiylashmasin.

### So‘ralgan yozuvdan chiqmaslik

So‘rov: “Faqat lotin yozuvida javob bering. Ushbu jumlani ma’nosini o‘zgartirmay lotinga o‘giring: Ўзбекистонда сунъий интеллект воситаларидан фойдаланиш.”

Kutilgan matn: “O‘zbekistonda sun’iy intellekt vositalaridan foydalanish.” Kirill harflari qolib ketmaganini va ma’no o‘zgarmaganini tekshiring. Sinovni o‘z sohangiz atamalari va uydirma shaxsiy ma’lumotlar bilan takrorlang.

### Aralash til va yetishmayotgan ma’lumot

So‘rov: “Mijoz ‘zakaz tayyormi, bugun olib ketsam bo‘ladimi?’ deb yozdi. Sizda buyurtma holati haqida ma’lumot yo‘q. Lotin yozuvida qisqa javob yozing va kerakli aniqlashtiruvchi savolni bering.”

Mos javob buyurtma raqami yoki boshqa zarur ma’lumotni so‘raydi. Buyurtma tayyorligini va’da qilmasligi yoki olib ketish vaqtini o‘ylab topmasligi kerak. Tizimingiz buyurtma holatini tekshira olsa, shu integratsiyani alohida sinang.

### Berilgan manbaga tayangan holda javob berish

Vosita uchun qisqa, maxfiy bo‘lmagan hujjat tayyorlang. Hujjatda javobi bor bitta va javobi yo‘q bitta savol bering. Vosita dalil bilan tasdiqlangan ma’lumotni yetishmayotgan ma’lumotdan ajratishini tekshiring. Qidiruv ilovasida yakuniy javob bilan birga topilgan parchalarni ham saqlang. Shunda xato qidiruvda yoki javob tuzishda yuz berganini aniqlash osonlashadi.

## 5. Tanlovdan oldin amaliy cheklovlarni tekshiring

- **Kirish imkoniyati:** servis siz turgan joyda va kerakli qurilmada ishlashini tekshiring. Foydalanmoqchi bo‘lgan hisob yoki API tarifining o‘zini sinang.
- **Maxfiylik:** provayderning ma’lumotlardan foydalanish va ularni saqlash bo‘yicha amaldagi shartlarini o‘qing. Ruxsat berilmagan servisga mijozlar bazasi, kirish kalitlari, tibbiy yoki boshqa maxfiy ma’lumotlarni yuklamang. Tanlash bosqichida uydirma yoki shaxsiy qismlari olib tashlangan misollardan foydalaning.
- **Litsenziyalar:** model, asosiy model, ma’lumotlar to‘plami va kod litsenziyalarini alohida tekshiring. Model vaznlari yoki faylni yuklab olish mumkinligi undan istalgan maqsadda foydalanishga ruxsat borligini anglatmaydi. Hugging Face [model kartalari qo‘llanmasida](https://huggingface.co/docs/hub/model-cards) litsenziya va baholash ma’lumotlari qayerda ko‘rsatilishini tushuntiradi.
- **Joylashtirish:** mahalliy model uchun xotira talabi, dasturiy bog‘liqliklar va qurilmangizdagi tezlikni tekshiring. `trust_remote_code` kabi sozlamalarni yoqishdan oldin modelga qo‘shilgan kodni ko‘rib chiqing.
- **Budjet:** bepul sinov, davriy limit, obuna va foydalanilgan hajmga qarab to‘lanadigan APIni farqlang. Limit qachon yangilanishi, nimalar kiritilgani, limitdan oshganda nima bo‘lishi, soliqlar va to‘lov imkoniyatlarini provayderdan tekshiring. Ro‘yxatdagi belgi aniq limitni kafolatlaydi, deb hisoblamang.
- **Boshqa vositaga o‘tish:** ishlaringizni eksport qilish, saqlangan ma’lumotlarni o‘chirish va butun jarayonni qayta qurmasdan provayderni almashtirish imkoniyatlarini tekshiring.

## 6. Qarorni qayd eting

- Tanlangan vazifa va foydalanuvchilar:
- Solishtirilgan variantlar va sinov sanasi:
- Model yoki mahsulot versiyalari va sozlamalar:
- Sinov misollari va aniqlangan xatolar:
- Tekshirgan kishi va qolgan til muammolari:
- Hali tekshirilishi kerak bo‘lgan maxfiylik va litsenziya masalalari:
- Kutiladigan foydalanish hajmi va xarajat chegarasi:
- Tanlangan variant va tanlov sababi:
- Qaysi o‘zgarishlardan keyin qayta solishtirish kerak:

Amaldagi talablaringizga javob beradigan va tekshirishga maqbul mehnat talab qiladigan variantni tanlang. Model o‘zgarsa, yangi turdagi ma’lumot qo‘shilsa, narx sezilarli o‘zgarsa yoki foydalanuvchilarga ta’sir qiladigan xato yuz bersa, tanlovni qayta tekshiring.

## Qo‘llanma haqida

2026-yil 8-oktabrda tayyorlangan. Ushbu ro‘yxatni mustaqil AI servisiga ega GPTBot.uz jamoasi yuritadi. GPTBot.uz OpenAI bilan bog‘liq emas. Tanlash mezonlari GPTBot.uz va raqobatchi servislar uchun bir xil; ro‘yxatga kiritilish tavsiya yoki ustunlik isboti hisoblanmaydi.

Repozitoriyning [CC0 litsenziyasi](../LICENSE) uning o‘z materiallariga tegishli. Havola berilgan servislar, modellar, ma’lumotlar to‘plamlari va kodlar o‘z shartlarini saqlab qoladi. Tuzatish va takliflar uchun [hissa qo‘shish qoidalari](../CONTRIBUTING.md) bilan tanishing.
