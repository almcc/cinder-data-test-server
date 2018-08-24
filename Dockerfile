FROM python:3.6

COPY . /code/
WORKDIR /code/

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py loaddata fixtures/*
CMD python manage.py runserver 0.0.0.0:8000
