import os
import mongoengine
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


default_config = {'MONGODB_SETTINGS': {
    'db': 'test',
    'host': 'localhost',
    'port': 27017,

}}

heroku_config = {'MONGODB_SETTINGS:': {
    'db': 'gjgapi',
    'host': 'mongodb+srv://root:aD1gEy5BsNJFG2Wy@cluster0.cci75.mongodb.net/Cluster0?retryWrites=true&w=majority'
}}

# init flask
app = Flask(__name__)

api = Api(app=app)

#create endpoints
create_routes(api=api)

MONGO_URI = os.environ.get('MONGO_URI')

print(MONGO_URI)
if not MONGO_URI:
    #MONGO_URL = 'mongodb+srv://' + urllib.parse.quote('root') + ':' + urllib.parse.quote('aD1gEy5BsNJFG2Wy') + '@cluster0.cci75.mongodb.net/Cluster0?retryWrites=true&w=majority'
    config = default_config
    app.config.update()

else:
    config = heroku_config
    app.config.update()

db = MongoEngine()
db.init_app(app)

#  mongoengine.connect(**default_config['MONGODB_SETTINGS'])
db = get_db()
print("db name", db.name)
if __name__ == '__main__':
    app.run(debug=True)






