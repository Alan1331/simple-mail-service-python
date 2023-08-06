from flask import request
from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.utils.validator import validate_mail_id
from app.models.mails import Mail
from app.models.users import User

class SingleMailResource(Resource):
    @jwt_required()
    @validate_mail_id
    def get(self, mail_id):
        result = Mail.get_mail_by_id(mail_id)

        if result != None:
            return {
                'message': 'requested mail was successfully received',
                'result': result
            }, 200
        else:
            return {'message': 'The mail is not found'}, 404
        
    @jwt_required()
    @validate_mail_id
    def delete(self, mail_id):
        result = Mail.delete_mail(mail_id)

        if result.acknowledged:
            if result.deleted_count == 1:
                return {
                    'message': 'The mail with given ID was deleted',
                    'mail_id': mail_id
                }, 200
            else:
                return {
                    'message': 'The mail with given ID is not found',
                    'mail_id': mail_id
                }, 200
        else:
            return {
                'message': 'The delete operation could not be performed due to database error'
            }, 500