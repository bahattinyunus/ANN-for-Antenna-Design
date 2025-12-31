# 02 - Matematiksel Model ve ANN Analizi

Bu doküman, projede kullanılan Yapay Sinir Ağı (ANN) modelinin matematiksel altyapısını ve elektromagnetik formülizasyon ile ilişkisini detaylandırır.

## 1. Fiziksel Denklem Temeli
Yama antenin rezonans frekansı ($f_r$) klasik olarak şu formülle tahmin edilir:
$$f_r = \frac{c_0}{2L \sqrt{\epsilon_{eff}}}$$
Burada $\epsilon_{eff}$ (Etkin Dielektrik Sabiti), sızma alanlarını (fringing effects) hesaba katan bir düzeltme katsayısıdır:
$$\epsilon_{eff} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left[ 1 + 12 \frac{h}{W} \right]^{-1/2}$$

## 2. Neden ANN? (Problem Karmaşıklığı)
Yukarıdaki formüller sadece dikdörtgen ve basit yapılar içindir. Karmaşık geometrilerde, Maxwell denklemlerinin analitik çözümü imkansız hale gelir. ANN, bu noktada bir **"Universal Approximator"** olarak devreye girer.

## 3. ANN Katman Yapısı (MLP)
Modelimiz, girdi parametrelerini doğrusal olmayan bir şekilde çıktıya haritalar:
- **Girdi Vektörü:** $X = [W, L, h, \epsilon_r]$
- **Ağırlıklı Toplam ($z$):** $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$
- **Aktivasyon ($\sigma$):** $a^{(l)} = \text{ReLU}(z^{(l)})$

Model, milyonlarca simülasyon çıktısını analiz ederek, fiziksel denklemlerin içine gizlenmiş karmaşık ilişkileri "öğrenir".

---
*Hazırlayan: Bahattin Yunus Çetin*
