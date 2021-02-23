from model.users import users
import json
from bson import json_util

ranking_dict = {}

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
    for doc in cursor: print(doc)
    json_docs = [json.dumps(doc, default=json_util.default) for doc in cursor]
    return json_docs

def insert_ranking_dict(object,points):
    display_name = object.display_name
    ranking_dict[display_name] = points
    x = dict(sorted(ranking_dict.items(), key=lambda item: item[1]))
    temp = list(x.items())
    res = [idx for idx, key in enumerate(temp) if key[0] == display_name]
    print(res)
    return x