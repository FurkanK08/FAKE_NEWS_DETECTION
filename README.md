🧠 FAKE NEWS DETECTION with BERT (Türkçe)

Bu proje, Türkçe haberlerin doğruluğunu tespit edebilmek için BERT tabanlı bir sınıflandırma modeli kullanır.Amaç; haberin sahte (fake) mi yoksa doğru (gerçek) mi olduğunu otomatik olarak belirlemektir.

📂 Proje Yapısı

Uygulama/
├── backend/
│   ├── app.py                  # API servisi (FastAPI)
│   ├── bert_model/             # BERT modeli (Google Drive’dan manuel eklenmeli)
├── frontend/                   # Kullanıcı arayüzü (isteğe bağlı)
├── requirements.txt            # Gerekli Python kütüphaneleri
└── README.md

🔧 Gereksinimler

pip install -r requirements.txt

Not: transformers, torch, fastapi, uvicorn, pydantic, firebase-admin gibi paketleri içerir.

🚀 Projeyi Çalıştırmak

bert_model klasörünü indir 👇📁 Google Drive - [Model Dosyası](https://drive.google.com/drive/folders/1X8PxFMatv4QaQfT8-nUZneUysIVmGkSj?usp=sharing)

İndirdiğin bert_model klasörünü şu dizine yerleştir:

Uygulama/backend/bert_model/

Ardından FastAPI backend servisini başlat:

cd Uygulama/backend
uvicorn app:app --reload

API arayüzüne tarayıcıdan eriş:

http://127.0.0.1:8000/docs

🌟 Özellikler

✅ Türkçe BERT modeli

✅ Sahte haber tespiti

✅ FastAPI ile REST API

✅ Kolay entegrasyon

✅ Google Drive ile model paylaşımı

🔒 Notlar

bert_model klasörü, büyük dosya boyutundan dolayı GitHub’a yüklenmemiştir.Lütfen yukarıdaki Google Drive bağlantısından indirip projeye manuel olarak ekleyin.
