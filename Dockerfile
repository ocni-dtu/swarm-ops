FROM python:3.6.10-alpine

COPY src /app

CMD ["celery", "worker", "-A", "settings"]