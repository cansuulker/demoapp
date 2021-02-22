# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from api.sort_ranking import sort_ranking_pipeline,insert_ranking_dict
# project resources
from model.users import users

pipeline = [
    {
        "$project": {
            "_id": 1,
            "rank": "$rank",
            "point": "$point",
            "display_name": "$display_name",
            "country": "$country",
        }
    },
        {
        "$sort": {
            "point": -1
        }
    },

    {
        "$group": {
            "_id": {},
            'arr': {
                "$push": {
                    "rank": "$rank",
                    "point": "$point",
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
            'arr.point': -1
        }
    },   {
        "$project": {
            "_id": 0,
            "rank": '$arr.rank',
            "point": '$arr.point',
            "display_name": '$arr.display_name',
            "country": '$arr.country',
        }
    }

]




class usersapi(Resource):

    def get(self, user_id: str) -> Response:
        ''' GET response for a single user in the collection
            :returns JSON object
            GET /user/profile/{guid}
        '''
        get_user = users.objects.get(user_id=user_id)
        output = {'user_id': str(get_user.user_id),
                  'display_name': str(get_user.display_name),
                  'points': get_user.points,
                  'rank': get_user.rank
                  }
        return jsonify({'result': output})

    def delete(self, user_id: str) -> Response:
        ''' DELETE response for deleting a single user
            :returns JSON object
        '''
        output = users.objects(user_id=user_id).delete()
        return jsonify({'result': output})

class userscreateapi(Resource):
    def post(self) -> Response:
        ''' POST response for creating a user
            :returns JSON object
            POST /user/create
        '''
        data = request.get_json(force=True)
        post_user = users(**data)
        num_users = users.objects.count()
        post_user.rank = num_users + 1
        post_user.points = 0
        post_user.save()
        insert_ranking_dict(post_user,0)
        output = {'user_id': str(post_user.id),
                  'display_name': str(post_user.display_name),
                  'points': post_user.points,
                  'rank': post_user.rank
                  }
        return jsonify({'result': output})

class leaderboardapi(Resource):
    def get(self) -> Response:
        ''' GET response for all users in the collection
            :returns JSON object
            GET /leaderboard
        '''

        output = users.objects().order_by('rank')
        return jsonify({'result': output})

class leaderboardcountryapi(Resource):
    def get(self, country: str) -> Response:
        ''' GET response for all users in the collection with specific country code
            :returns JSON object
            GET /leaderboard/{country_iso_code}
        '''
        output = users.objects(country=country)
        return jsonify({'result': output})

class scoresubmitapi(Resource):
    def post(self) -> Response:
        ''' POST response for updating a user's score
            :returns JSON object
            POST /score/submit
        '''
        data = request.get_json(force=True)
        display_name = data["display_name"]
        score_worth = data["score_worth"]
        curr_user = users.objects.get(display_name=display_name)
        uid = curr_user.user_id
        points = curr_user.points
        total_points = score_worth + points
        if curr_user is None:
            output = 'No user with user_id:' + uid
        else:
            users.objects(user_id=uid).update_one(points=total_points)
            insert_ranking_dict(curr_user, total_points)
            output = sort_ranking_pipeline(users)
            print(output)
            output = {'score_worth': score_worth,
                      'user_id':   str(uid),
                      'timestamp': str(curr_user.date_modified)
                     }
        return jsonify({'result': output})

