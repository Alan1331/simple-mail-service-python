from flask import request
from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.utils.validator import is_valid_object_id
from app.models.mails import Mail
from app.models.users import User

class SingleMailResource(Resource):
    @jwt_required()
    def get(self, mail_id):
        if not is_valid_object_id(mail_id):
            return {'message': 'Invalid mail id'}, 400

        result = Mail.get_mail_by_id(mail_id)

        if result != None:
            return {
                'message': 'requested mail was successfully received',
                'result': result
            }, 200
        else:
            return {'message': 'The mail is not found'}, 404