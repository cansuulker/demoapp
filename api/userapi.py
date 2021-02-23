# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from tools.sort_ranking import sort_ranking_pipeline
from tools.csv_to_json import csv_to_json
# project resources
from model.users import users

class usersapi(Resource):

    def get(self, user_id: str) -> Response:
        ''' GET response for a single user in the collection
            :returns JSON object
            GET /user/profile/{guid}/
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
            POST /user/create/
        '''
        data = request.get_json(force=True)
        post_user = users(**data)
        num_users = users.objects.count()
        post_user.rank = num_users + 1
        post_user.points = 0
        post_user.save()
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
            GET /leaderboard/
        '''

        output = users.objects().order_by('rank')
        return jsonify({'result': output})

class leaderboardcountryapi(Resource):
    def get(self, country: str) -> Response:
        ''' GET response for all users in the collection with specific country code
            :returns JSON object
            GET /leaderboard/{country_iso_code}/
        '''
        output = users.objects(country=country)
        return jsonify({'result': output})

class scoresubmitapi(Resource):
    def post(self) -> Response:
        ''' POST response for updating a user's score
            :returns JSON object
            POST /score/submit/
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
            ranking = sort_ranking_pipeline(users,display_name) + 1
            users.objects(user_id=uid).update_one(points=total_points, rank=ranking)
            output = {'score_worth': score_worth,
                      'user_id':   str(uid),
                      'timestamp': str(curr_user.date_modified)
                     }
        return jsonify({'result': output})


class usersbulkinsertapi(Resource):
   def post(self) -> Response:
        ''' POST response for multiple users
            :returns JSON object
            POST /user/bulk_insert/
        '''
        array = csv_to_json('/Users/cansuulker/PycharmProjects/GJGApi/resources/sample_user_data.csv',
                            '/Users/cansuulker/PycharmProjects/GJGApi/resources/sample_user_data.json')
        user_instances = [users(**data) for data in array]

        users.objects.insert(user_instances, load_bulk=False)
        output = user_instances.count()
        return jsonify({'Sample user data loaded': output})