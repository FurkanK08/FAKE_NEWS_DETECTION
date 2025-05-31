from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from transformers import BertTokenizer, BertForSequenceClassification, BertConfig
from safetensors.torch import load_file
import torch
import os

app = FastAPI()

# Statik dosyalar (CSS, JS, HTML)
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# Model yükleme (bert_model dizininden)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_path = os.path.join(os.path.dirname(__file__), "bert_model")

# 1. Config yükle
config = BertConfig.from_json_file(os.path.join(model_path, "config.json"))

# 2. Boş model oluştur
model = BertForSequenceClassification(config)

# 3. Safetensors state_dict yükle
state_dict = load_file(os.path.join(model_path, "model.safetensors"))
model.load_state_dict(state_dict)
model.to(device)
model.eval()

# 4. Tokenizer yükle
tokenizer = BertTokenizer.from_pretrained(model_path)

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    text = data.get("text", "")

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        fake_prob = probs[0][1].item()
        real_prob = probs[0][0].item()

    label = "Fake" if fake_prob > 0.5 else "Real"
    return JSONResponse(content={
        "label": label,
        "fake_prob": round(fake_prob * 100, 2),
        "real_prob": round(real_prob * 100, 2)
    })
