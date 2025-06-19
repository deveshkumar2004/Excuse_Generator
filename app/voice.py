import os
from gtts import gTTS
from datetime import datetime

def text_to_speech(text: str, language: str = "en", save_path: str = None) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if save_path is None:
        output_dir = "audio"
        os.makedirs(output_dir, exist_ok=True)
        filename = f"excuse_{timestamp}.mp3"
        save_path = os.path.join(output_dir, filename)
    else:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

    tts = gTTS(text, lang=language)
    tts.save(save_path)
    return save_path
