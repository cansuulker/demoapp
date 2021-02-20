# flask packages
from flask_restful import Api

# project resources
from api.userapi import usersapi, leaderboardapi, leaderboardcountryapi,scoresubmitapi,userscreateapi


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(leaderboardapi,'/leaderboard/', endpoint='leaderboard')
    api.add_resource(leaderboardcountryapi, '/leaderboard/<country>/', endpoint='leaderboard country')

    api.add_resource(scoresubmitapi, '/score/submit/', endpoint='score submit')
    api.add_resource(usersapi, '/user/profile/<user_id>/', endpoint='user profile')
    api.add_resource(userscreateapi, '/user/create/', endpoint='user create')
