import requests
import logging
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

def translate_text(text: str, target_lang: str) -> str:
    if target_lang == "hi":
        try:
            translated = translator(text)[0]['translation_text']
            return translated
        except Exception as e:
            logging.error(f"Translation error: {e}")
            return f"[Translation error: {str(e)}] {text}"
    return text

def generate_apology(scenario: str, urgency: str, language: str = "en") -> str:
    prompt = (
        f"Only output a sincere apology in one sentence for this scenario: {scenario} with urgency level: {urgency}. "
        "Do not include introductions, examples, or any explanation. Just the apology itself."
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
            },
            timeout=10
        )

        english_apology = response.json().get("response", "").strip().strip('\"')

        final_apology = translate_text(english_apology, language)

        return final_apology

    except Exception as e:
        logging.error(f"Error generating apology: {e}")
        return f"Error generating apology: {str(e)}"
