import os
import mongoengine
import ssl
import urllib
from mongoengine.connection import get_db, connect
from flask import Flask, app
from flask_restful import Resource, Api
from flask import make_response
from flask_mongoengine import MongoEngine
from bson.json_util import dumps
import os


# project resources
from api.userapi import usersapi
from api.routes import create_routes
from config import Config



'''default_config = {'MONGODB_SETTINGS': {
    'db': 'test',
    'host': 'localhost',
    'port': 27017,

}}'''

default_config = {'MONGODB_SETTINGS:': {
    'db': 'users',
    'host': 'mongodb+srv://admin:arU1TensYAUHbzVB@gjgapi.wfht1.mongodb.net/users?retryWrites=true&w=majority'
}}

# init flask
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app=app)

#create endpoints
create_routes(api=api)

MONGO_URI = os.environ.get('MONGO_URI')
if not MONGO_URI:
     MONGO_URI = 'mongodb+srv://' + urllib.parse.quote('admin') + ':' + urllib.parse.quote('arU1TensYAUHbzVB') + '@gjgapi.wfht1.mongodb.net/users?retryWrites=true&w=majority'


'''if not MONGO_URI:
    config = heroku_config
    app.config.update()

else:
    config = heroku_config
    app.config.update()'''

db = MongoEngine()
#db.config = {'MONGODB_SETTINGS:': {
#    'db': 'users',
#    'host': 'mongodb+srv://admin:arU1TensYAUHbzVB@gjgapi.wfht1.mongodb.net/users?retryWrites=true&w=majority'
#}}
print(db.config)
db.init_app(app)

db = get_db()
print("db name", db.name)
if __name__ == '__main__':
    app.run(debug=True)






