# 🌐 Dil Tespiti

Bu, girdiğiniz metnin dilini bigram, trigram ve dörtgram frekanslarına göre belirleyen basit bir dil tespiti uygulamasıdır. Proje, GUI için Tkinter ve farklı diller için n-gram frekanslarını içeren CSV dosyalarını kullanır.

## ✨ Özellikler
- Girdiğiniz metnin dilini tespit eder.
- İngilizce, Almanca, Fransızca, İspanyolca, Portekizce ve İtalyanca dillerini destekler.
- Tespit edilen dilin bayrağını gösterir.

## 🎥 Video Tanıtımı

Proje de kullanılan yöntemin ve uygulamanın nasıl çalıştığını gösteren bir videoyu aşağıdaki bağlantıdan izleyebilirsiniz:

[Proje Tanıtım Videosu](https://www.youtube.com/watch?v=XzPeBvLuVzA)

## 📦 Kurulum

1. Depoyu klonlayın:
    ```sh
    git clone https://github.com/mfurkanolcer/language-detection.git
    cd language-detection
    ```

2. Gerekli Python paketlerini yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

3. Gerekli CSV dosyalarının ve resimlerin doğru dizinlerde olduğundan emin olun:
    ```
    language_detection/
    ├── data/
    │   ├── english.csv
    │   ├── german.csv
    │   ├── french.csv
    │   ├── spanish.csv
    │   ├── portuguese.csv
    │   └── italian.csv
    ├── img/
    │   ├── english.png
    │   ├── german.png
    │   ├── french.png
    │   ├── spanish.png
    │   ├── portuguese.png
    │   └── italian.png
    ```

## 🚀 Kullanım

Uygulamayı çalıştırın:
```sh
python app.py
```
 
## 🖼️ GUI Genel Bakış

-     Metin Girişi: Dilini tespit etmek istediğiniz metni girin.
-     Çalıştır Butonu: Dil tespit algoritmasını çalıştırmak için tıklayın.
-     Sonuç Kutusu: Tespit sonuçlarını gösterir.
-     Sıfırla Butonu: Giriş ve sonuç alanlarını temizler.
-     Dil Bayrağı: Tespit edilen dilin bayrağını gösterir.

## 📸 Ekran Görüntüleri
### Ana Pencere
![Screenshot_1](https://github.com/mfurkanolcer/nlp-project/assets/58481075/597d7430-1e8a-4680-8bfe-c9ff7c4381da)

### Tespit Sonucu
![Screenshot_2](https://github.com/mfurkanolcer/nlp-project/assets/58481075/d6b80f05-adda-4534-b649-196f02b5cb51)

## 🛠️ Nasıl Çalışır

1. **Frekansları Okuma:** Uygulama, n-gram frekanslarını CSV dosyalarından okur.
2. **Frekansları Hesaplama:** Girdi metindeki n-gramların frekanslarını hesaplar.
3. **Mesafeleri Hesaplama:** Bu frekansları CSV dosyalarındaki referans frekanslarla karşılaştırır.
4. **Dili Tespit Etme:** En yüksek benzerliğe sahip dili tespit eder ve gösterir.

## 📊 Veri Yapısı

N-gram frekanslarını depolamak için kullanılan veri yapısı:

```python
language_data = {
    "ENGLISH": {
        "BIGRAM_STRINGS": [...],
        "TRIGRAM_STRINGS": [...],
        "QUADGRAM_STRINGS": [...],
        "FREQUENCY_BIGRAM": [...],
        "FREQUENCY_TRIGRAM": [...],
        "FREQUENCY_QUADGRAM": [...]
    },
    ...
}
```
