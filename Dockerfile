FROM python:3.6

COPY . /code/
WORKDIR /code/

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py import_cars dataset.csv
RUN mkdir -p static
CMD gunicorn --workers=9 -b 0.0.0.0:8000 --access-logfile - core.wsgi
