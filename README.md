# Event-Driven IoT Security System

A lightweight, containerized Flask server that listens for motion events (e.g. from Reolink cameras), flashes a Govee smart light, logs the event, and sends a Discord alert.

---

## 🚀 Features

- 🟢 `/motion` endpoint for receiving motion alerts
- 💡 Govee light flashes on event
- 🔐 Trusted IP filtering
- 📝 Local file logging of motion events
- 📣 Discord webhook notifications
- 🐳 Dockerized for portability

---

## 📁 Project Structure

```
event-driven-iot-security/
├── app/
│   ├── main.py
│   ├── govee_controller.py
│   ├── logger.py
│   └── .env               # Not tracked (excluded in .gitignore)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/event-driven-iot-security.git
cd event-driven-iot-security
```

### 2. Create `.env` in `app/`

```env
GOVEE_API_KEY=your_govee_api_key
GOVEE_DEVICE_ID=your_device_id
GOVEE_MODEL=your_model
TRUSTED_IPS=127.0.0.1,::1,172.18.0.1
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_id/your_token
```

### 3. Build & Run with Docker

```bash
docker-compose up --build
```

---

## 🧪 Testing

### Flash the Govee Light

```bash
curl -X POST http://localhost:5000/flash
```

### Simulate a Motion Event

```bash
curl -X POST http://localhost:5000/motion \
  -H "Content-Type: application/json" \
  -d '{"camera":"test_cam","event":"motion_detected","timestamp":"2025-06-13T18:00:00Z"}'
```

---

## 🛡️ Security Notes

- IPs not in `TRUSTED_IPS` will be rejected with 403 errors.
- `.env` is used for storing secrets securely.
- Only expose this service publicly if secured behind a reverse proxy with TLS and auth.

---

## 📘 Use Cases

- 🔐 Home security notifications
- 🏠 Smart lighting triggers
- 🧪 IoT and automation prototyping
- 📂 DevSecOps/Cloud security portfolio project

---

## ✍️ Author

**Armando Cardona**  
🔗 [LinkedIn](https://www.linkedin.com/in/armando-cardona)  
💼 DevSecOps • Secure Automation • Cloud Security  
