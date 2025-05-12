# Intelligent Excuse Generator  
### *With Emergency Alerts, Voice Output, PDF Proofs, Auto Scheduling, and Smart Ranking*

---

## 📌 Project Overview  
The **Intelligent Excuse Generator** is a backend-driven AI solution built with **FastAPI** that intelligently creates contextual and language-specific excuses for real-life situations. It incorporates advanced features such as:

- Real-time **emergency alert triggering**
- **Voice output** and **PDF generation**
- **Multi-language** support and translation
- Automated **scheduling** of excuses
- A **smart ranking system** for excuse prioritization

---

## ⚙️ Technologies Used
- **Python 3.12**
- **FastAPI** – API framework
- **Uvicorn** – ASGI server
- **gTTS** – Google Text-to-Speech
- **ReportLab** – For PDF proof generation
- **Ollama + LLaMA2** – Language model integration
- **Langdetect & Googletrans** – Language detection and translation
- **APScheduler** – Job scheduling
- **Custom Ranking Engine**

---

## 📁 Project Structure
```bash
intelligent_excuse_backend/ app/
├── main.py          # FastAPI entry point
├── generator.py     # Excuse generation logic
├── models.py        # Pydantic models
├── storage.py       # Local storage and retrieval
├── proof.py         # PDF generation logic
├── voice.py         # Text-to-speech generation
├── emergency.py     # Emergency trigger handling
├── apology.py       # Apology generator
├── scheduler.py     # Job scheduling
└── ranker.py        # Excuse ranking logic
├── audio/
├── fonts/
├── proofs/
├── excuses.json
├── requirements.txt
└── README.md
```



---

## 🌟 Key Features
1. **AI-Powered Excuse Generation**
2. **Automated Scheduling via APScheduler**
3. **Emergency Alert System** (Text or Voice)
4. **Text-to-Speech Output with Language Translation**
5. **Professional PDF Proof Creation**
6. **Smart Ranking of Excuses Based on Context**
7. **History Logging of Generated Excuses**

---

## 📡 Sample API Requests

### 🔹Generate Excuse  
**`[POST] /generate_excuse/`**  
```json
{
  "scenario": "I was late for class",
  "urgency": "high",
  "language": "en"
}
```
###🔹Trigger Emergency Alert

**`[POST] /trigger-emergency/`**
```json
{
  "method": "text",
  "description": "My leg was injured from falling"
}
```
##🚀 How to Run

**`Create a virtual environment`**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies
```

```bash

pip install -r requirements.txt
Start Ollama with LLaMA2
```

```bash
ollama run llama2
Run FastAPI server
```

```bash
uvicorn app.main:app --reload
```

### 🔹 Access API Docs

Open your browser and go to: http://127.0.0.1:8000/docs

---

## 📝 Final Note

This project simulates intelligent excuse automation with real-world applicability. From contextual excuse generation to automated scheduling and emergency responses, it showcases a robust backend AI system that blends functionality with innovation.

