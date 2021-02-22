from model.users import users
import json
from bson import json_util

ranking_dict = {}

def sort_ranking_pipeline(model):

    pipeline = [
    {
        "$project": {
            "_id": 1,
            "rank": "$rank",
            "points": "$points",
            "display_name": "$display_name",
            "country": "$country",
        }
    },
        {
        "$sort": {
            "points": -1
        }
    },

    {
        "$group": {
            "_id": {},
            'arr': {
                "$push": {
                    "rank": "$rank",
                    "points": "$points",
                    "display_name": "$display_name",
                    "country": "$country"
                }
            }
        }
    }, {
        "$unwind": {
            "path": '$arr',
            "includeArrayIndex": 'rank',
        }
    }, {
        "$sort": {
            'arr.points': -1
        }
    },   {
        "$project": {
            "_id": 0,
            "rank": '$arr.rank',
            "points": '$arr.points',
            "display_name": '$arr.display_name',
            "country": '$arr.country',
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
    dict(sorted(ranking_dict.items(), key=lambda item: item[1]))
    print(ranking_dict)
    return ranking_dict