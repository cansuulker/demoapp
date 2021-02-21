import os
import urllib.parse
import ssl
import mongoengine
from mongoengine.connection import get_db, connect
from flask import Flask, app
from flask_restful import Resource, Api
from flask import jsonify
from flask_pymongo import PyMongo
from flask import make_response
from pymongo import MongoClient
from flask_mongoengine import MongoEngine
from bson.json_util import dumps
import os
import urllib.parse
from api.userapi import usersapi
from api.routes import create_routes

default_config = {'MONGODB_SETTINGS': {
    'db': 'test_db',
    'host': 'localhost'
 #   'port': 27017,
 #   'username': 'admin',
  #  'password': 'password',
  #  'authentication_source': 'admin'
}}

# init flask
app = Flask(__name__)

api = Api(app=app)
create_routes(api=api)

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    #MONGO_URL = 'mongodb+srv://' + urllib.parse.quote('root') + ':' + urllib.parse.quote('aD1gEy5BsNJFG2Wy') + '@cluster0.cci75.mongodb.net/Cluster0?retryWrites=true&w=majority'
    config = default_config
    app.config.update()



#db = MongoEngine(app=app)
db = MongoEngine()
db.init_app(app)

#  mongoengine.connect(**default_config['MONGODB_SETTINGS'])
db = get_db()
print("db name", db.name)
if __name__ == '__main__':
    app.run(debug=True)






