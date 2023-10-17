FROM python:3.11-slim

COPY ./src /src
WORKDIR /src

RUN pip3 install --no-cache-dir -r requirements.txt