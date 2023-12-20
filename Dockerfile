FROM python:3.10.3-bullseye

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

