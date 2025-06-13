import os
import requests

def send_discord_notification(event):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        return

    content = f"📹 **Motion Detected**\n```{event}```"
    data = {"content": content}

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("✅ Discord notification sent.")
    except requests.RequestException as e:
        print(f"❌ Failed to send Discord notification: {e}")
