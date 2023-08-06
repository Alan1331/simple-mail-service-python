from flask_restful import Api

from app.resources.users import UsersResource
from app.resources.user import SingleUserResource

def register_routes(api: Api):
    api.add_resource(UsersResource, '/api/users')
    api.add_resource(SingleUserResource, '/api/users/<string:mail_address>')