from flask import request
from flask_restful import Resource

from app.models.users import User

class SingleUserResource(Resource):
    def get(self, mail_address):
        result = User.get_user_by_mail_address(mail_address)

        if result != None:
            return {
                'message': 'Requested user was successfully received',
                'result': result
            }, 200
        else:
            return {'message': 'The user is not found'}, 404
        
    def delete(self, mail_address):
        result = User.delete_user(mail_address)

        if result.acknowledged:
            if result.deleted_count == 1:
                return {
                    'message': 'The user with given mail_address was deleted'
                }, 200
            else:
                return {
                    'message': 'The user with given mail_address is not found'
                }, 404
        else:
            return {
                'message': 'The delete operation could not be performed due to database error'
            }, 500