import json
from datetime import datetime
import os

EXCUSE_FILE = "excuses.json"

def load_excuses():
    if not os.path.exists(EXCUSE_FILE):
        return []
    with open(EXCUSE_FILE, "r") as f:
        return json.load(f)

def save_excuse(scenario,ranking, urgency, excuse):
    data = load_excuses()
    data.append({
        "scenario": scenario,
        "ranked": ranking,
        "urgency": urgency,
        "excuse": excuse,
        "timestamp": datetime.now().isoformat()
    })
    with open(EXCUSE_FILE, "w") as f:
        json.dump(data, f, indent=4)