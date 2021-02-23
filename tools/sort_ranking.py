'''
MongoDB Aggregation Pipeline method
:param MongoEngine document class, display_name attribute for users()
:returns users ranking based on points
'''

from model.users import users
import json
from bson import json_util

def sort_ranking_pipeline(model,display_name):
    pipeline = [
    {
        "$project": {
            "_id": 1,
            "points": "$points",
            "display_name": "$display_name",
            "country": "$country"
        }
    },
    {
        "$sort": {
            "points": -1
        }
    },

        {
            "$group": {
                "_id": 0,
                "users": {
                    "$push": {
                        "_id": "$_id",
                        "points": "$points",
                        "display_name": "$display_name",
                        "country": "$country"
                    }
                }
            }
        },
        {
            "$unwind": {
                "path": "$users",
                "includeArrayIndex": "ranking"
            }
        },
        {
            "$match": {
                "users.display_name": display_name
            }
        }
]
    cursor = model.objects().aggregate(pipeline)
    for doc in cursor:
        result = doc['ranking']
    #json_docs = [json.dumps(doc, default=json_util.default) for doc in cursor]
    return result

