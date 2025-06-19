from datetime import datetime
import os
from app.voice import text_to_speech

def generate_emergency_alert(description: str) -> dict:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    text_message = f"🚨 Emergency Alert 🚨\nTime: {timestamp}\nDetails: {description}"
    os.makedirs("alerts", exist_ok=True)
    
    text_path = os.path.join("alerts", f"alert_{timestamp}.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text_message)

    with open("alerts/emergency_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(text_message + "\n\n")

    voice_message = (
        f" Hello, this is an emergency  call. Can you please tell me what the emergency is?\n"
        f"{description}\n"
        f" Alright, noted. Please stay calm. Help is on the way. Stay safe and take care."
    )

    os.makedirs("calls", exist_ok=True)
    voice_path = text_to_speech(
        voice_message,
        language="en",
        save_path=os.path.join("calls", f"call_{timestamp}.mp3")
    )

    return {
        "text_alert": text_path,
        "voice_alert": voice_path,
        "message": "Emergency alert triggered with text and realistic voice call."
    }
