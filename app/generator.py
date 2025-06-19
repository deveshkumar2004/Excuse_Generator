import requests
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

def translate_text(text: str, target_lang: str) -> str:
    if target_lang == "hi":
        translated = translator(text)[0]['translation_text']
        return translated
    return text

def generate_excuse(scenario: str, urgency: str = "moderate", language: str = "en") -> str:
    prompt = (
        f"Only output a short and realistic excuse (max 100 words) for this scenario: {scenario}. "
        "Do not include greetings, introductions, or apologies. Just the excuse."
    )
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.8,
                    "num_predict": 100
                }
            }
        )
        english_excuse = response.json()["response"].strip().strip('\"')

        final_excuse = translate_text(english_excuse, language)
        return final_excuse
    except Exception as e:
        return f"Error generating excuse: {str(e)}"
