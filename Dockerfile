FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
ADD .env.docker /code/.env

EXPOSE 8000
CMD python manage.py migrate; python manage.py runserver 0.0.0.0:8000
