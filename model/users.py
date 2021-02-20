import uuid
from mongoengine import *
from flask_mongoengine import MongoEngine
import mongoengine_goodjson as gj


class users(gj.Document):

    user_id = StringField(required=True,primary_key=True,unique=True)
    display_name = StringField(required=True)
    point = IntField()
    rank = IntField()
    country = StringField(required=True)
    def generate_uuid(self):
        self.user_id = uuid.uuid4()
