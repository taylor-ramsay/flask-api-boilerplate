FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /api
WORKDIR /api

ENV FLASK_ENV=development

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "api.views.main", "--reload"]