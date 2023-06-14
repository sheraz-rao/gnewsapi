FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN apt update && apt-get install -y supervisor 
RUN pip install --upgrade pip -r requirements.txt 
