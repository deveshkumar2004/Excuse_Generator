from datetime import datetime, timedelta
import json
import os

def predict_next_absence():
    if not os.path.exists("excuses.json"):
        return None

    try:
        with open("excuses.json", "r") as f:
            data = json.load(f)

        timestamps = [entry.get("timestamp") for entry in data if "timestamp" in entry]
        times = [datetime.fromisoformat(ts) for ts in timestamps if ts]

        if not times:
            return None

        hours = [t.hour for t in times]
        most_common_hour = max(set(hours), key=hours.count)

        now = datetime.now()
        next_time = now.replace(hour=most_common_hour, minute=0, second=0, microsecond=0) + timedelta(days=1)

        return next_time
    except Exception as e:
        print("❌ Prediction error:", e)
        return None
