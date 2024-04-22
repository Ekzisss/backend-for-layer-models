FROM python:3.11

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt