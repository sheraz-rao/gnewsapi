FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
RUN mkdir /code/static
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "GNewsAPI.wsgi:application"]
# CMD [ "gunicorn", "GNewsAPI.wsgi:application --bind", "0.0.0.0:8000" ]
