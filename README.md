# Django-Splunk Test Project

## Intention
This project demonstrates how we can "stream" data from django project's database to [splunk](https://www.splunk.com)

Data is streamed in 2 ways here:
1. Via management command *load2splunk*
2. Via celery task on each **.save()** call of *Product* model

## Prerequisites
- Install [docker-compose](https://docs.docker.com/compose/)
- Run `docker-compose up -d`
- Run `pip install -r requirements.txt`

## Environment
- Run `cp .env.example .env`
- Fill *.env* file with relevant data

## Fixtures
- Run `python manage.py migrate`
- Run `python manage.py loaddata fixtures/fixtures.json`

## Running
### Celery Beat
- Run `celery -A config beat -l info`

### Celery worker
- Run `celery -A config  worker -l info`

### Webserver
- Run `python manage.py runserver 0.0.0.0:8080`

### Push existing data into Splunk
- Run `python manage.py load2splunk`
