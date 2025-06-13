# Smart Home Motion Triggered Security (Pure Python Edition)

## 🛡 Overview
This project listens for motion alerts from a Reolink IP camera and triggers a Govee smart light using the official HTTPS API. Everything runs locally, securely, and is containerized with Docker.

## 📦 Features
- Flask-based webhook API
- Secure Govee light trigger via HTTPS
- Logs events to local JSON file
- Dockerized app running as non-root
- Environment-based config and IP filtering

## 🚀 Setup

```bash
cp app/.env.example app/.env
# Edit the .env file with your Govee details and trusted IPs

docker-compose up --build
```

## 🔐 Security Practices
- Environment-based secrets management
- Runs as non-root user in Docker
- Filters motion triggers by IP
- Logs stored locally

## 🔄 Future Ideas
- Add SQLite logging
- Create Grafana dashboard for event timeline
- Support additional smart devices