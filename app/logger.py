import json
from datetime import datetime

def log_event(event):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event
    }
    with open("logs/events.json", "a") as f:
        json.dump(entry, f)
        f.write("\n")