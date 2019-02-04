ARG platform=library
FROM ${platform}/python:alpine

WORKDIR /app
COPY requirements.txt ./
RUN apk --no-cache add build-base libffi-dev openssl-dev && \
    pip install -r requirements.txt && \
    rm /app/requirements.txt && \
    apk --no-cache del build-base libffi-dev openssl-dev && \
    apk --no-cache add libffi openssl
COPY main.py message_filter.py botActions.py tokens.py ./

ENV PYTHONPATH=/app/
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

CMD python main.py