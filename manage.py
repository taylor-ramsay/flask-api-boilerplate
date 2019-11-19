from flask_script import Manager
from api.core.application import application
from api.core.database import db

manager = Manager(application)


@manager.command
def initdb():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()