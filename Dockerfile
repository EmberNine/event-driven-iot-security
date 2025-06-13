FROM python:3.11-slim

WORKDIR /app

COPY app/ ./
COPY requirements.txt .
RUN touch motion_log.txt && chmod 666 motion_log.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m nonrootuser
USER nonrootuser

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-", "main:app"]
