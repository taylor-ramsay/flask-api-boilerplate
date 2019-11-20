# Flask Api Boilerplate
This is a minimal standalone flask api using Docker, Postgres, sqlalchemy, and gunicorn.

To get started:

- Edit .env file with database details.

- To build the api run:  `docker-compose build`

- To start the api run: `docker-compose up`

- To initialize the database, enter the shell: `docker exec -it api sh`, and run `manage.py initdb`
