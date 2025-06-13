FROM python:3.11-slim

WORKDIR /app

COPY app/ ./
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m nonrootuser
USER nonrootuser

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]