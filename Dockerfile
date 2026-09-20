FROM python:3.14-alpine

WORKDIR /app
COPY requirements.txt ./
RUN apk --no-cache add build-base libffi-dev openssl-dev jpeg-dev zlib-dev freetype-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    rm /app/requirements.txt && \
    apk --no-cache del build-base libffi-dev openssl-dev && \
    apk --no-cache add libffi openssl
COPY golfillobot/ ./golfillobot

ENV PYTHONPATH=/app/ PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8

CMD ["python3", "golfillobot/main.py"]
