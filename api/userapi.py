# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource

# project resources
from model.users import users

class usersapi(Resource):

    def get(self, user_id: str) -> Response:
        ''' GET response for a single user in the collection
            :returns JSON object
            GET /user/profile/{guid}
        '''
        output = users.objects.get(user_id=user_id)
        return jsonify({'result': output})

    def delete(self, user_id: str) -> Response:
        ''' DELETE response for deleting a single user
            :returns JSON object
        '''
        output = users.objects(id=user_id).delete()
        return jsonify({'result': output})

class userscreateapi(Resource):
    def post(self) -> Response:
        ''' POST response for creating a user
            :returns JSON object
            POST /user/create
        '''
        data = request.get_json()
        post_user = users(**data).save()
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})

class leaderboardapi(Resource):
    def get(self) -> Response:
        ''' GET response for all users in the collection
            :returns JSON object
            GET /leaderboard
        '''
        output = users.objects()
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
    def put(self, score_worth: int, user_id: str) -> Response:
        ''' PUT response for updating a user's score
            :returns JSON object
            POST /score/submit
        '''
        data = request.get_json()
        put_user = users.objects(id=user_id).update(**data)
        output = {'id': str(put_user.id)}
        return jsonify({'result': output})