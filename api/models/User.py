from api.core.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), unique=True, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name
        }
    
    def get_all_users():
        return [User.json(user) for user in User.query.all()]
    
