from flask import Flask, request, jsonify
from govee_controller import trigger_govee_light
from logger import log_event
import os

app = Flask(__name__)

@app.route('/motion', methods=['POST'])
def handle_motion():
    event = request.get_json()
    source_ip = request.remote_addr

    if source_ip not in os.getenv("TRUSTED_IPS", "").split(","):
        return jsonify({"error": "Unauthorized source"}), 403

    log_event(event)
    trigger_govee_light()
    return jsonify({"status": "triggered"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)