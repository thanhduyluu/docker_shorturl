FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt requirement.txt

RUN pip install -r requirements.txt

COPY . .
