import csv
import random
from mongoengine import NotUniqueError, ValidationError
from model import users
from tools.mongo_wrapper import mongo

@mongo
def generate_test_users(filepath: str = 'resources/sample_user_data.csv', delimiter: str = ','):
    """
    Converts data in csv file to documents in user collection.
    Uses @mongo wrapper to connect via mongoengine during execution.
    Randomly generates fav_meals list and access__admin parameters.
    :param filepath:
    :param delimiter:
    :return:
    """
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=',')

        for datum in data:
            try:
                user = users(**datum, __auto_convert=True)
                # generate random admin access, password, and favorite meals
                user.save()
                print(f"Added: {user.user_id} | {user.country} ")
            except NotUniqueError:
                print(f'Invalid Entry: {user.user_id} is already taken.')



