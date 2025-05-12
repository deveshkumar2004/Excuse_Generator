# Intelligent Excuse Generator

### _With Emergency Alerts, Voice Output, PDF Proofs, Auto Scheduling, and Smart Ranking_

---

## Project Overview

The **Intelligent Excuse Generator** is a backend-driven AI solution built with **FastAPI** that intelligently creates contextual and language-specific excuses for real-life situations. It incorporates advanced features such as:

- Real-time **emergency alert triggering**
- **Voice output** and **PDF generation**
- **Multi-language** support and translation
- Automated **scheduling** of excuses
- A **smart ranking system** for excuse prioritization

---

## Technologies Used

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

## Project Structure

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

## Key Features

1. **AI-Powered Excuse Generation**
2. **Automated Scheduling via APScheduler**
3. **Emergency Alert System** (Text or Voice)
4. **Text-to-Speech Output with Language Translation**
5. **Professional PDF Proof Creation**
6. **Smart Ranking of Excuses Based on Context**
7. **History Logging of Generated Excuses**

---

## Sample API Requests

### Using Postman to Test the API

Follow these steps to interact with your backend using Postman:

### Step 1: Download Postman App fron here-->https://www.postman.com/downloads/

### Step 2: Make Requests in Postman
-->  After Login Click on my workplace
-->  Then go to new
-->  follow below steps for diffrent scenario

### 1.  Generate an Excuse

Method: POST

URL: http://127.0.0.1:8000/generate_excuse/

Body → raw → JSON

```json
{
  "scenario": "I missed my exam due to health issues",
  "urgency": "high",
  "language": "en"
}
```

```json
 Response:
{
  "excuse": "I was sick and couldn’t make it to the exam.",
  "proof_file": "proofs/proof_2025-05-12_16-10-23.pdf",
  "audio_file": "audio/excuse_2025-05-12_16-10-23.mp3"
}
```

### 2. Trigger Emergency

Method: POST

URL: http://127.0.0.1:8000/trigger-emergency/

Body → raw → JSON

```json
{
  "method": "text",
  "description": "My leg was injured from falling"
}
```

## How to Run

```bash
Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

```bash
Install dependencies
pip install -r requirements.txt
```
### download Ollama from here-->https://ollama.com/download/windows

```bash
Start Ollama with LLaMA2
ollama run llama2

```

```bash
Run FastAPI server
uvicorn app.main:app --reload

The API will be running at:
 http://127.0.0.1:8000 --reload
```

### Access API Docs

Open your browser and go to: http://127.0.0.1:8000/docs

---

## Final Note

This project simulates intelligent excuse automation with real-world applicability. From contextual excuse generation to automated scheduling and emergency responses, it showcases a robust backend AI system that blends functionality with innovation.
