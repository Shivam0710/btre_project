FROM python:3.8.3-slim-buster

WORKDIR /btre

COPY requirements.txt /btre/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

COPY . /btre/