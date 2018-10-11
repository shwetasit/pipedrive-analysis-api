from flask import Blueprint
from flask_restful import Api


user_blueprint = Blueprint('user', __name__)
user_blueprint_api = Api(user_blueprint)


from resource.user import UserListAPI
user_blueprint_api.add_resource(UserListAPI, '/user')

