# 📰 Fake News Detector – BERT Destekli Web Uygulaması

Bu proje, BERT tabanlı bir metin sınıflandırma modelini kullanarak haberlerin **sahte mi yoksa gerçek mi** olduğunu tespit eden bir web uygulamasıdır.  
Frontend (HTML/CSS/JS) ile kullanıcıdan haber metni alınır, FastAPI backend üzerinden modele gönderilir ve sonuç renkli olarak gösterilir.

---

## 🚀 Özellikler

- 📥 Kullanıcıdan metin girişi
- 🧠 BERT modeli ile sınıflandırma
- ✅ Sonuç: Fake / Real (oranlı)
- 🟩 Gerçek: Yeşil bildirim  
- 🟥 Sahte: Kırmızı bildirim

---

## 🧱 Dosya Yapısı

Uygulama/
├── backend/
│ ├── app.py
│ ├── bert_model/
│ │ ├── config.json
│ │ ├── model.safetensors
│ │ ├── vocab.txt
│ │ └── tokenizer_config.json vs.
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── requirements.txt
└── README.md 


---

## ⚙️ Kurulum

### 1. Ortamı Kur

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt 

### Uygulamayı başlat
cd backend
uvicorn app:app --reload
