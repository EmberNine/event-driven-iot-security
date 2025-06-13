import requests
import os

def trigger_govee_light():
    url = "https://developer-api.govee.com/v1/devices/control"
    headers = {
        "Govee-API-Key": os.getenv("GOVEE_API_KEY"),
        "Content-Type": "application/json"
    }
    payload = {
        "device": os.getenv("GOVEE_DEVICE_ID"),
        "model": os.getenv("GOVEE_MODEL"),
        "cmd": {
            "name": "turn",
            "value": "on"
        }
    }
    try:
        response = requests.put(url, json=payload, headers=headers)
        print("Govee response:", response.text)
    except Exception as e:
        print("Error triggering Govee light:", e)