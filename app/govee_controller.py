import os
import requests
import time

GOVEE_API_KEY = os.getenv("GOVEE_API_KEY")
DEVICE_ID = os.getenv("GOVEE_DEVICE_ID")
MODEL = os.getenv("GOVEE_MODEL")
HEADERS = {
    "Govee-API-Key": GOVEE_API_KEY,
    "Content-Type": "application/json"
}
BASE_URL = "https://developer-api.govee.com/v1/devices/control"

def send_command(command):
    data = {
        "device": DEVICE_ID,
        "model": MODEL,
        "cmd": command
    }
    response = requests.put(BASE_URL, headers=HEADERS, json=data)
    return response.status_code, response.text

def flash_govee_light():
    off_cmd = {"name": "turn", "value": "off"}
    on_cmd = {"name": "turn", "value": "on"}

    for _ in range(2):
        code, resp = send_command(off_cmd)
        print(f"Flashed Govee light: off → Response: {code}")
        time.sleep(0.5)
        code, resp = send_command(on_cmd)
        print(f"Flashed Govee light: on → Response: {code}")
        time.sleep(0.5)
