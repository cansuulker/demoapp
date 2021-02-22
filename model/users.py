import uuid
from mongoengine import *
import datetime
from flask_mongoengine import MongoEngine
import mongoengine_goodjson as gj

class users(Document):

    user_id = StringField(required=True, default=lambda: str(uuid.uuid4()))
    display_name = StringField(required=True,unique=True)
    points = IntField()
    rank = IntField()
    country = StringField(required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
    score_worth = IntField()

    def generate_uuid(self):
        self.user_id = uuid.uuid4()
