

from mongoengine.connection import get_db, connect
from flask import Flask, app
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine


# project resources
from api.userapi import usersapi
from api.routes import create_routes
from config import Config

#For local connections
default_config = {'MONGODB_SETTINGS': {
    'db': 'test',
    'host': 'localhost',
    'port': 27017,


}}


# init flask
app = Flask(__name__)

#For Heroku connection
app.config.from_object(Config)
api = Api(app=app)

#create endpoints
create_routes(api=api)

db = MongoEngine()

db.init_app(app)

db = get_db()
print("db name", db.name)
if __name__ == '__main__':
    app.run(debug=True)






