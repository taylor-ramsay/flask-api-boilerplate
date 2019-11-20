from flask_sqlalchemy import SQLAlchemy
import os

from api.core.application import application


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()

application.config.from_object(config)

db = SQLAlchemy(application)