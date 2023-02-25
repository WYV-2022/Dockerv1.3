FROM python:3.9.16

ENV PYTHONUNBUFFRED=1

WORKDIR /code2

COPY . .

COPY reqs.txt .

RUN pip install -r reqs.txt