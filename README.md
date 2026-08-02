# AI Akademi

Yapay zekâyı sıfırdan öğretmek için hazırlanmış bir Flask web uygulaması.
Kullanıcılar kayıt olur, tarihsel + teorik derslerden oluşan modülleri
okur, her modül sonunda kısa bir quiz çözer ve gerçek bir yapay zekâ
modeliyle (Claude, Anthropic API üzerinden) sohbet ederek pratik yapar.

## Özellikler

- Kayıt / giriş sistemi (Flask-Login, şifreler hashlenir)
- 5 modüllük müfredat: YZ tarihi (1943-1993), makine öğrenmesi temelleri,
  sinir ağları ve derin öğrenme, Transformer'lar ve LLM'ler
- Her modül sonunda otomatik puanlanan quiz
- Kullanıcıya özel ilerleme takibi (panel / dashboard)
- Gerçek AI API'si ile çalışan soru-cevap chatbot'u
- **Premium (10 TL, tek seferlik):** normalde bir modülü açmak için bir
  önceki modülün quiz'ini bitirmen gerekir. Premium alan kullanıcı tüm
  modüllere sırayı beklemeden anında erişir. iyzico Ödeme Formu ile
  çalışır.

## Premium / iyzico Kurulumu

1. [iyzico Merchant Panel](https://merchant.iyzipay.com)'e kayıt ol (test
   için sandbox hesabı yeterli, sandbox panel: sandbox-merchant.iyzipay.com).
2. Panelde **Ayarlar > API Anahtarları** bölümünden `api_key` ve
   `secret_key` değerlerini al.
3. `.env` dosyanda `IYZICO_API_KEY` ve `IYZICO_SECRET_KEY`'i doldur.
   Teste devam ederken `IYZICO_BASE_URL=sandbox-api.iyzipay.com` kalsın;
   canlıya geçince `api.iyzipay.com` yap ve gerçek (canlı) anahtarları gir.
4. iyzico'nun sandbox test kartlarıyla (panel dokümantasyonunda listeli,
   örn. `5528790000000008`) ödeme akışını uçtan uca dene.
5. Fiyatı değiştirmek istersen `app.py` içindeki `PREMIUM_PRICE`
   değişkenini güncelle.

> Not: iyzico, T.C. kimlik numarası dahil bazı alıcı bilgilerini zorunlu
> kılar (bu regülasyon gereği, uygulamanın tercihi değil). Ödeme sayfasına
> geçmeden önce kullanıcıdan bu bilgileri kısa bir formla alıyoruz; kart
> bilgilerinin kendisi hiçbir zaman bizim sunucumuza gelmez, doğrudan
> iyzico'nun barındırdığı ödeme sayfasında girilir.

## Yerelde Çalıştırma

```bash
# 1) Sanal ortam oluştur (önerilir)
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2) Bağımlılıkları kur
pip install -r requirements.txt

# 3) Ortam değişkenlerini ayarla
cp .env.example .env
# .env dosyasını aç, SECRET_KEY'i rastgele bir değerle değiştir
# ve kendi ANTHROPIC_API_KEY'ini gir (console.anthropic.com üzerinden alınır)

# 4) Uygulamayı başlat
python app.py
```

Tarayıcıda `http://localhost:5000` adresine git.

> Not: `ANTHROPIC_API_KEY` girilmezse site normal çalışır, sadece sohbet
> sayfası "API anahtarı tanımlı değil" uyarısı gösterir; dersler ve
> quiz'ler API olmadan da tam çalışır.

## Yayımlama (Deploy Etme)

Bu bir standart Flask uygulaması olduğu için birçok yerde ücretsiz/ucuz
şekilde yayımlanabilir. En kolay üç seçenek:

### Render.com (önerilen, ücretsiz katman var)
1. Projeyi bir GitHub reposuna yükle.
2. Render.com'da "New Web Service" seç, reponu bağla.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Environment sekmesinde `SECRET_KEY` ve `ANTHROPIC_API_KEY` değişkenlerini gir.

(`gunicorn` üretimde çalıştırmak için gerekir: `pip install gunicorn` ve
`requirements.txt`'e ekle.)

### Railway.app
Render'a çok benzer akış: GitHub reposunu bağla, ortam değişkenlerini
gir, Railway otomatik olarak `Procfile` veya start command'ı algılar.
Bir `Procfile` eklemek istersen:
```
web: gunicorn app:app
```

### PythonAnywhere
Flask uygulamaları için hazır şablonları var, küçük projeler için
ücretsiz katmanı yeterli olur; dosyaları yükleyip WSGI dosyasında
`app.py`'deki `app` nesnesini göstermen yeterli.

## Notlar

- Veritabanı olarak SQLite kullanılıyor (`aiacademy.db`), küçük/orta
  ölçekli kullanım için yeterlidir. Daha büyük trafik beklersen
  `SQLALCHEMY_DATABASE_URI`'yi Postgres gibi bir veritabanına
  çevirebilirsin.
- `SECRET_KEY`'i asla varsayılan değerde bırakma; yayımlamadan önce
  mutlaka rastgele, uzun bir değerle değiştir.
- `.env` dosyasını **asla** GitHub'a yükleme (`.gitignore`'a ekli).
