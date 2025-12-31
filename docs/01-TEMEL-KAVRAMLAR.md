# 01 - Temel Kavramlar (Anten Teorisi)

Bu doküman, mikroşerit yama antenlerin temel çalışma prensiplerini ve projenin fiziksel dayanağını açıklar.

## 1. Mikroşerit Yama Anten Nedir?
Mikroşerit antenler, dielektrik bir tabaka (substrat) üzerinde yer alan ince bir metal yama (patch) ve alt kısmındaki toprak düzleminden (ground plane) oluşur. Düşük profil, kolay üretim ve hafiflik parametreleri nedeniyle günümüz kablosuz iletişim sistemlerinde (5G, Wi-Fi, Uydu) standart hale gelmiştir.

## 2. Geometrik Parametreler ve Etkileri
- **Yama Genişliği ($W$):** Genellikle giriş empedansını ve ışıma paternini kontrol eder.
- **Yama Uzunluğu ($L$):** Rezonans frekansının ana belirleyicisidir. Genellikle rezonans frekansındaki dalga boyunun yarısı ($\lambda/2$) civarındadır.
- **Substrat Yüksekliği ($h$):** Antenin bant genişliğini ve verimini etkiler. Yükseklik arttıkça bant genişliği artar ancak yüzey dalgaları kaybı çoğabilir.
- **Dielektrik Sabiti ($\epsilon_r$):** Malzemenin elektrik özelliklerini belirler. $\epsilon_r$ arttıkça anten boyutları küçülür (minyatürleştirme) ancak verim düşebilir.

## 3. Elektromanyetik Davranış
Anten, besleme hattından gelen enerjiyi uzaya elektromanyetik dalga olarak yayar. Yama ile toprak düzlemi arasında oluşan elektrik alan, kenarlardan sızarak (fringing fields) ışıma oluşturur. Bu "sızma" etkisi, antenin elektriksel uzunluğunun fiziksel uzunluğundan biraz daha fazla olmasına neden olur ($\Delta L$).

---
*Bu doküman Bahattin Yunus Çetin tarafından projenin teorik altyapısını güçlendirmek için hazırlanmıştır.*
