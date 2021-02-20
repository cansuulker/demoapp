from mongoengine import *

class leaderboard(Document):
    rank = IntField(required=True)
    points = IntField(required=True)
    display_name = StringField(required=True,primary_key=True,unique=True)
    country = StringField()


