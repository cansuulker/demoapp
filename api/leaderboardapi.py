from flask import Response, request, jsonify
from flask_restful import Resource

from model.leaderboard import leaderboard

class leaderboardapi(Resource):

    def get(self) -> Response:
        output = leaderboard.objects()
        return jsonify({'result': output})


