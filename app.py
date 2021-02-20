import os
import urllib.parse
import ssl
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


# init flask
app = Flask(__name__)

api = Api(app=app)
create_routes(api=api)


MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = 'mongodb+srv://' + urllib.parse.quote('root') + ':' + urllib.parse.quote('aD1gEy5BsNJFG2Wy') + '@cluster0.cci75.mongodb.net/Cluster0?retryWrites=true&w=majority'

db = MongoEngine(app=app)

if __name__ == '__main__':
    app.run(debug=True)




