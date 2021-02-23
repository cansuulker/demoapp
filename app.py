import os
import mongoengine
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


'''default_config = {'MONGODB_SETTINGS': {
    'db': 'test',
    'host': 'localhost',
    'port': 27017,

}}'''

heroku_config = {'MONGODB_SETTINGS:': {
    'db': 'users',
    'host': 'mongodb+srv://admin:arU1TensYAUHbzVB@gjgapi.wfht1.mongodb.net/users?retryWrites=true&w=majority'
}}

# init flask
app = Flask(__name__)
api = Api(app=app)

#create endpoints
create_routes(api=api)

MONGO_URI = os.environ.get('MONGO_URI')
if not MONGO_URI:
     MONGO_URI = 'mongodb+srv://' + urllib.parse.quote('admin') + ':' + urllib.parse.quote('arU1TensYAUHbzVB') + '@gjgapi.wfht1.mongodb.net/users?retryWrites=true&w=majority'

print(MONGO_URI)
'''if not MONGO_URI:
    config = heroku_config
    app.config.update()

else:
    config = heroku_config
    app.config.update()'''

db = MongoEngine()
db.init_app(app)

#  mongoengine.connect(**default_config['MONGODB_SETTINGS'])
db = get_db()
print("db name", db.name)
if __name__ == '__main__':
    app.run(debug=True)






