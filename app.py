
import os
import urllib.parse
import uuid
import ssl
from flask import Flask
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask import make_response
from pymongo import MongoClient

from bson.json_util import dumps

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
     MONGO_URL = 'mongodb+srv://' + urllib.parse.quote('root') + ':' + urllib.parse.quote('aD1gEy5BsNJFG2Wy') + '@cluster0.cci75.mongodb.net/Cluster0?retryWrites=true&w=majority'

app = Flask(__name__)
client = MongoClient(MONGO_URL,ssl_cert_reqs=ssl.CERT_NONE)


uid = uuid.uuid4()
displayname = 'gjg_0'

userDocument = {
  "user_id": uid,
  "display_name": displayname,
  "point": 0,
  "rank": 1,
}

db = client.gjgapi

users = db.users
users.insert_one(userDocument)


#app.config['MONGO_URI'] = MONGO_URL
#mongo = PyMongo(app)

#def output_json(obj, code, headers=None):
#    resp = make_response(dumps(obj), code)
#    resp.headers.extend(headers or {})
#    return resp

#DEFAULT_REPRESENTATIONS = {'application/json': output_json}
#api = Api(app)
#api.representations = DEFAULT_REPRESENTATIONS

