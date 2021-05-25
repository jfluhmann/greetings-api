# syntax=docker/dockerfile:1

FROM python:3.9.5-alpine3.13

COPY requirements.txt  /app/requirements.txt

RUN apk --no-cache add --virtual build-dependencies \
      build-base \
      gcc 

RUN apk -q --no-cache add mariadb-connector-c \
      mariadb-dev \
      && pip install -qq -r /app/requirements.txt \
      && rm -rf .cache/pip \
      && apk del build-dependencies

COPY ./app /app

# EXPOSE 80

CMD uvicorn app.main:app --host 0.0.0.0 --port 80
