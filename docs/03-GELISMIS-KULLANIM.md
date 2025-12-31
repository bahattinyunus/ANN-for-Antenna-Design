# 03 - Gelişmiş Kullanım ve Optimizasyon

Anten tasarımında Yapay Zeka kullanımını bir üst seviyeye taşımak isteyenler için ileri düzey teknikler.

## 1. Veri Kalitesi ve Genişletme
`generator.py` içindeki parametre aralıklarını (`uniform distribution`) değiştirerek farklı teknoloji standartlarına (örn: Rogers substratlar için düşük $\epsilon_r$, Seramikler için yüksek $\epsilon_r$) odaklanabilirsiniz.

## 2. Hiperparametre Optimizasyonu
`model.py` içindeki `hidden_layer_sizes` parametresi ile oynayarak modelin kapasitesini test edin:
- Daha fazla nöron = Daha yüksek karmaşıklık kapasitesi (Ancak overfitting riski).
- Daha fazla katman = Daha derin soyutlama (Ancak vanishing gradient riski).

## 3. Tersine Mühendislik (Inverse Modeling)
Projemiz şu an boyutlardan frekans tahmin ediyor ($Physical \rightarrow Frequency$).  Ancak asıl "büyü", hedef frekansı verip boyutları bulmaktadır ($Frequency \rightarrow Physical$).
**Yöntem:**
1. Geçerli modeli eğitin.
2. Bir optimizasyon algoritması (Genetic Algorithm veya Particle Swarm) kullanarak, hedeflenen $f_r$ değerine en yakın çıktıyı veren girdi $W, L$ setini bulun.

## 4. Model Dağıtımı (Deployment)
Eğitilen `antenna_model.pkl` dosyasını bir Flask veya FastAPI servisine entegre ederek, anten tasarımcıları için gerçek zamanlı bir web-tool oluşturabilirsiniz.

---
*Geleceğin anten tasarımcıları için, Bahattin Yunus Çetin.*
