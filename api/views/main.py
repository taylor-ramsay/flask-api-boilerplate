from flask import request, jsonify

from api.core.application import application
from api.core.database import db
from api.models.User import User

@application.route("/ping")
def index():
    return "pong"

@application.route("/create-user", methods=['POST'])
def create():
    email = request.json["email"]
    name = request.json["name"]
    db.session.add(User(email=email, name=name))
    db.session.commit()
    return jsonify({ 'users': User.get_all_users() })
