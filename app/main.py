from flask import Flask, request, jsonify
from govee_controller import flash_govee_light
from logger import log_event
from notifier import send_discord_notification
import os

app = Flask(__name__)

@app.route('/motion', methods=['POST'])
def handle_motion():
    event = request.get_json()
    source_ip = request.remote_addr
    trusted_ips = os.getenv("TRUSTED_IPS", "").split(",")

    print(f"📡 Motion trigger received from: {source_ip}")
    print(f"🔐 Trusted IPs: {trusted_ips}")

    if source_ip not in trusted_ips:
        print("❌ Unauthorized access attempt blocked.")
        return jsonify({"error": "Unauthorized source"}), 403

    print("✅ Authorized motion event received.")
    log_event(event)
    send_discord_notification(event)  # ✅ DISCORD ALERT
    flash_govee_light()
    return jsonify({"status": "triggered"}), 200

@app.route('/flash', methods=['POST'])
def flash_light():
    flash_govee_light()
    return jsonify({"status": "flashed"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
