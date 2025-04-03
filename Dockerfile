FROM python:3.10.8-slim-buster
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y gcc libffi-dev musl-dev ffmpeg aria2

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD gunicorn app:app & python3 main.py
