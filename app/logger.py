import os
from datetime import datetime

def log_event(event):
    # Ensure the log is written to a path inside the container's working directory
    log_filename = "motion_log.txt"
    log_path = os.path.join(os.getcwd(), log_filename)

    # Format event with timestamp
    timestamp = datetime.utcnow().isoformat()
    log_entry = f"[{timestamp}] Camera: {event.get('camera')}, Event: {event.get('event')}, Raw: {event}\n"

    try:
        with open(log_path, "a") as log_file:
            log_file.write(log_entry)
        print(f"📝 Logged event: {log_entry.strip()}")
    except Exception as e:
        print(f"❌ Failed to log event: {e}")
