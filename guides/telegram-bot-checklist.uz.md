# O‘zbekcha Telegram botini ishga tushirish: amaliy tekshiruv ro‘yxati

[English](telegram-bot-checklist.md) · [Resurslar ro‘yxati](../README.uz.md) · [O‘zbek tili uchun AI tanlash](choosing-uzbek-ai.uz.md)

O‘zbekcha yoki o‘zbekcha-ruscha botga haqiqiy foydalanuvchilarni taklif qilishdan oldin ushbu ro‘yxatdan foydalaning. U AI funksiyasi bo‘lishi mumkin bo‘lgan kichik birinchi versiyaga mo‘ljallangan. Bu rejalashtirish va qabul qilish qo‘llanmasi; biror bot tekshiruvlardan o‘tganini tasdiqlamaydi.

## 1. Foydalanuvchi yakunlay oladigan bitta jarayonni belgilang

Foydalanuvchi nima qila olishini yozing: hujjatdagi ma’lumotni so‘rash, ariza qoldirish, buyurtmani tekshirish yoki bo‘sh vaqtga yozilish. Boshlanish nuqtasi, kerakli ma’lumotlar, tasdiqlash, saqlanadigan natija va keyingi mas’ul shaxsni ko‘rsating.

- Bot, uning mazmuni, texnik yordami va doimiy xarajatlari uchun mas’ullarni belgilang.
- Aniq qoida bo‘yicha ishlashi kerak bo‘lgan fakt va amallarni erkin matn bilan ishlashdan ajrating. Ombor qoldig‘i, narx, ruxsat va buyurtma holatini asosiy biznes tizimidan oling.
- Qaysi amallarda foydalanuvchi tasdig‘i kerakligini belgilang. Qabulga yozish, ma’lumotni o‘zgartirish yoki to‘lov olishdan oldin aniq tafsilotlarni ko‘rsating.
- Bot qachon aniqlashtiruvchi savol berishi, xodimga yo‘naltirishi yoki yordam bera olmasligini aytishini belgilang.
- Birinchi versiyaga kirmaydigan funksiyalarni qisqacha yozib qo‘ying. Bu sinov va xarajat hisobini aniqroq qiladi.

## 2. Egalikni rasmiylashtiring va kirish kalitlarini himoyalang

Botni rasmiy [BotFather](https://t.me/BotFather) orqali yarating va boshqaring. Telegramning [bot yaratish qo‘llanmasi](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) token olish va uni bekor qilishni tushuntiradi. Bot tokenini parol kabi himoya qiling.

- Ishlaydigan bot mas’ul egasi boshqaradigan hisobda bo‘lsin. Texnik xizmat uchun kirish qanday topshirilishini hujjatlashtiring.
- Sinov va haqiqiy foydalanish uchun alohida botlar, kalitlar va ma’lumotlardan foydalaning.
- Bot tokeni va model API kalitlarini maxfiy kalitlar omborida yoki himoyalangan ishga tushirish sozlamalarida saqlang. Ularni kod, skrinshot, ochiq muammo yozuvi yoki brauzerda ishlaydigan JavaScriptga joylamang.
- Jurnallar va xatolik hisobotlaridan kalitlarni, jumladan token qatnashgan URL manzillarini yashiring.
- Oshkor bo‘lgan tokenni bekor qilib, serverdagi kalitni yangilang. Uni fayldan o‘chirish tarqalgan nusxani yaroqsiz qilmaydi.
- Administratorga vazifasi uchun zarur bo‘lgan huquqlarnigina bering.

## 3. O‘zbekcha matnlar va bot vakolatini tayyorlang

- Tilni aniq tanlash imkonini bering. Tanlov menyular, xatoliklar va keyingi xabarlarda ham saqlansin.
- Lotin va kirill yozuvi, o‘/g‘ va tutuq belgilarining turli ko‘rinishlari, o‘zbekcha-ruscha aralash gaplar, ism va joy nomlarini sinang. Foydalanuvchining tilini ismiga qarab belgilamang.
- Tugma yozuvlarini qisqa va bir xil uslubda yozing. “Orqaga”, “Bekor qilish” va “Xodim bilan bog‘lanish” tugmalari hamma joyda tushunarli ishlasin.
- AI qismiga tasdiqlangan manbalarni bering. Har bir manbaning mas’uli va tekshirilgan sanasi bo‘lsin. Manbada javobi yo‘q savollarni ham sinang.
- Muhim matnni o‘zbek tilini yaxshi biladigan kishiga tekshirtiring. Misollarni misol deb belgilang; uydirma mijoz fikri, loyiha tarixi yoki baholash natijasini e’lon qilmang.
- Foydalanuvchi xabarlari va qidiruvdan topilgan hujjatlarni ishonchsiz kirish ma’lumoti deb ko‘ring. Botni boshqa foydalanuvchi ma’lumotini, maxfiy kalitni oshkor qilishga yoki ruxsatsiz amal bajarishga undaydigan so‘rovlarni sinang. Huquqlarni faqat promptda emas, dastur kodida ham tekshiring.

Model yoki servis tanlash uchun [AI qo‘llanmasi](choosing-uzbek-ai.uz.md) va [baholash to‘plamidan](../evaluations/README.md) foydalaning.

## 4. Xabarlarni uzilishdan keyin tiklanadigan tarzda qayta ishlang

Long polling yoki webhook usulidan birini tanlang; Telegram ikkalasini bir vaqtda ishlatishga ruxsat bermaydi. Webhookda `secret_token` orqali belgilangan `X-Telegram-Bot-Api-Secret-Token` sarlavhasini tekshiring. Takroriy hodisalarni `update_id` orqali aniqlang. Bu xususiyatlar [Bot API hujjatida](https://core.telegram.org/bots/api#getting-updates) bayon qilingan.

- Hodisa yo‘qolsa ariza yoki buyurtma ham yo‘qoladigan bo‘lsa, qabul qilinganini tasdiqlashdan oldin uni ishonchli saqlang.
- Qayta yetkazilgan xabar yoki takror bosilgan tugma xavfsiz ishlasin: bitta amal bitta biznes yozuvini yaratsin. Muhim yozish amallari uchun dastur darajasida takror bajarilishni to‘suvchi kalitdan foydalaning.
- Sekin model so‘rovlari va integratsiyalarni hajmi cheklangan navbatga qo‘ying. Kutish va qayta urinish chegaralarini, ish tugamasa ko‘rsatiladigan xabarni belgilang.
- Vaqtinchalik xatoda qayta urinish takroriy bron, to‘lov yoki bildirishnoma yaratmasin. “Bajarilmadi” bilan “natija noma’lum” holatlarini farqlang.
- Noto‘g‘ri format, qo‘llab-quvvatlanmaydigan fayl, foydalanuvchi botni bloklashi va servis uzilishi ishchi jarayonni to‘xtatib qo‘ymasligini tekshiring.
- Chiquvchi xabarlarni navbat bilan yuboring va limitga yetish xatolarini qayta ishlang. Cheksiz tezlikni taxmin qilish o‘rniga Telegramning amaldagi [xabar yuborish limitlarini](https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this) tekshiring.
- Bot guruhda ishlasa, amaldagi huquqlari va [maxfiylik rejimi](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get) bilan qaysi xabarlarni qabul qilishini tekshiring.

## 5. Ma’lumotlar bilan ishlashni tushunarli qiling

Ma’lumot so‘rashdan oldin nima va nima uchun kerakligini ayting. Botni kim boshqarishi va yordam uchun qayerga murojaat qilish mumkinligini ko‘rsating. Xabarlar model provayderi yoki boshqa biznes tizimiga yuborilsa, buni tushuntiring.

- Faqat vazifa uchun zarur maydonlarni yig‘ing. Dasturlash va qabul sinovlarida uydirma ma’lumotlardan foydalaning.
- Saqlash joyi, kirish huquqlari, saqlash muddati va o‘chirish tartibini belgilang. O‘chirish ishlashini amalda tekshiring.
- To‘liq xabar va fayllarni odatiy holatda jurnalga yozmang. Xatoni topish uchun yetarli, maxfiy qismlari yashirilgan texnik ma’lumot qoldiring.
- So‘ralgan xizmatga rozilik bilan reklama xabarlariga rozilikni ajrating. Ixtiyoriy bildirishnomalarni to‘xtatish usuli ishlasin.
- Bir foydalanuvchining tarixi, hujjati yoki biznes yozuvi boshqa foydalanuvchi chatiga chiqmasligini tekshiring.
- To‘lov olsangiz, usulni tanlashdan oldin Telegramning [moddiy tovarlar va xizmatlar](https://core.telegram.org/bots/payments) hamda [raqamli tovar va xizmatlar](https://core.telegram.org/bots/payments-stars) uchun alohida hujjatlarini tekshiring. To‘lov holatini serverda tasdiqlang; skrinshot yoki mijoz ilovasidagi muvaffaqiyat xabari to‘lov isboti emas.

## 6. Qabul sinovini o‘tkazing va natijalarni saqlang

Har bir holat uchun sana, versiya, kirish ma’lumoti, kutilgan va haqiqiy natija hamda tekshirgan kishini qayd eting. Quyidagi holatlar boshlang‘ich ro‘yxatdir; ular o‘lchangan natijalar yoki to‘liq xavfsizlik auditi emas.

- **Birinchi kirish:** `/start` botni tushuntiradi, til tanlashni taklif qiladi va asosiy vazifaga olib boradi.
- **Tilni almashtirish:** til o‘zgarganda keyingi tekshiruv xatolari va tasdiqlash xabarlari ham yangilanadi.
- **Ma’lumot yetishmasligi:** to‘liq bo‘lmagan so‘rovda bot javob to‘qish o‘rniga aniq savol beradi.
- **Orqaga qaytish va bekor qilish:** harakatlar tushunarli holatga qaytaradi; bekor qilish biznes yozuvini yaratmaydi.
- **Takroriy amal:** ikki marta bosish, qayta urinish yoki takroriy hodisa bir nechta buyurtma, ariza yoki bron yaratmaydi.
- **AI noaniqligi:** manbada javobi yo‘q savolda bot narx, mavjudlik yoki qoida to‘qimaydi; cheklovini aytadi yoki xodimga yo‘naltiradi.
- **Ajratilgan ma’lumot:** ikki sinov foydalanuvchisi bir-birining tarixi yoki yozuvlariga, hatto identifikatorni taxmin qilib ham, kira olmaydi.
- **Uzilish va qayta ishga tushirish:** model javob bermasligi, CRM uzilishi va ishchi jarayon qayta boshlanishida holatni tiklash mumkin; foydalanuvchiga haqiqiy holat ko‘rsatiladi.
- **Xodimga yo‘naltirish:** mas’ul kishi so‘rov va zarur kontekstni haqiqatan oladi; foydalanuvchi keyin nima bo‘lishini biladi.
- **Suiiste’mol va xarajat:** haddan tashqari uzun yoki takroriy so‘rovlar belgilangan cheklovlarga tushadi, maxfiy ma’lumot oshkor bo‘lmaydi.

To‘lov va boshqa muhim amallar uchun takroriy callback, bekor qilish va natijasi noma’lum holatlarni alohida sinang. Tiklash tartibi aniq bo‘lmaguncha bu funksiyani ishga tushirmang.

## 7. Yaratish xarajati bilan ishlatish xarajatini ajrating

Izohsiz bitta “bot narxi” o‘rniga vazifa hajmi bo‘yicha xarajatlar tarkibini so‘rang:

- **Bir martalik ishlar:** jarayonni loyihalash, o‘zbekchalashtirish, integratsiya, dasturlash, sinov, serverga joylashtirish va topshirish.
- **Doimiy infratuzilma:** hosting, ma’lumotlar bazasi, fayl saqlash, zaxira nusxalar va monitoring.
- **AIdan foydalanish:** kirish va chiqish hajmi, saqlanadigan suhbat konteksti, hujjat qidirish, nutqni qayta ishlash va zarur qayta urinishlar.
- **Boshqa provayderlar:** CRM obunasi, pullik APIlar, to‘lov komissiyalari va kerakli litsenziyalar.
- **Odamlar mehnati:** yordam ko‘rsatish, materiallarni yangilash, nosozliklarni bartaraf etish va keyingi yaxshilashlar.
- **Hisob shartlari:** kutiladigan suhbatlar soni, eng yuqori yuklama, tillar, kiritilgan funksiyalar, soliqlar va har bir provayderga kim to‘lashi.

Kam, kutilgan va yuqori foydalanish holatlarini hisoblang. Auditoriyani kengaytirishdan oldin taxminlarni pilotdagi haqiqiy sarf bilan almashtiring. Xarajat ogohlantirishlari va imkon bo‘lsa dastur darajasidagi qat’iy limitni belgilang.

Vazifa tarkibi bo‘yicha hisob misoli uchun rus tilidagi [Telegram bot narxi kalkulyatori](https://gptbot.uz/ru/kalkulyator-stoimosti-telegram-bota/) ishlab chiqish va taxminiy infratuzilma xarajatlarini ajratadi. **Aloqadorlik haqida:** uni ushbu ro‘yxatni yurituvchi GPTBot.uz jamoasi boshqaradi. Ko‘rsatilgan oraliqlar shu jamoaning rejalashtirish baholari; ular bozor mezoni yoki majburiy narx taklifi emas. Mustaqil ijrochilar takliflarini bir xil vazifa va istisnolar asosida solishtiring; model/API sarfi va boshqa obunalarni alohida tekshiring.

## 8. Mas’ul va ortga qaytish rejasi bilan ishga tushiring

- Kelishilgan kichik pilot auditoriyadan boshlang va natijani qachon ko‘rib chiqishni belgilang.
- O‘rnatilgan versiya, sinov dalillari va hal qilinmagan cheklovlarni qayd eting.
- Xatolar, javob vaqti, xodimga yo‘naltirishlar va sarfni kuzating. Webhookda kutilayotgan hodisalar va yetkazish xatolarini [getWebhookInfo](https://core.telegram.org/bots/api#getwebhookinfo) orqali tekshiring.
- Ogohlantirishlarni oladigan va botni qachon vaqtincha to‘xtatishni hal qiladigan kishini belgilang.
- Muhim amallarni o‘chirish, xodimga murojaat qilish xabariga o‘tish va oldingi ishlaydigan versiyani tiklash yo‘lini sinang.
- Nosozlikdan keyin sababini tuzating va funksiyani qayta ochishdan oldin tegishli sinovlarni takrorlang.

Kalitlar oshkor bo‘lsa, bir foydalanuvchining ma’lumoti boshqasiga chiqsa, muhim amallar takror bajarilsa yoki xatolar uchun mas’ul bo‘lmasa, botni tayyor deb belgilamang. Oddiy ssenariyning ishlashi tayyorgarlikning faqat bir qismidir.

## Qo‘llanma haqida

2026-yil 8-oktabrda tayyorlangan; Telegramga oid manbalar va kalkulyator sahifasi shu sanada tekshirilgan. Provayder imkoniyatlari va shartlari o‘zgarishi mumkin. GPTBot.uz mustaqil bo‘lib, OpenAI yoki Telegram bilan bog‘liq emas.

Repozitoriyning [CC0 litsenziyasi](../LICENSE) uning o‘z materiallariga tegishli. Tashqi servislar va dasturlar o‘z shartlarini saqlab qoladi. Tuzatishlar uchun [hissa qo‘shish qoidalaridan](../CONTRIBUTING.md) foydalaning.
