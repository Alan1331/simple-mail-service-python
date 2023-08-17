from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from app.models.users import User

class LoginResource(Resource):
    def post(self):
        mail_address = request.form['mail_address']
        input_password = request.form['password']
        
        user_data = User.get_user_by_mail_address(user_mail_address=mail_address)

        if user_data != None:
            stored_password = user_data['password']

            if input_password == stored_password:
                access_token = create_access_token(identity=mail_address)
                return {
                    'message': 'User logged in successfully',
                    'access_token': access_token
                }, 200
            else:
                return {'message': 'Wrong password'}, 401
        
        else:
            return {'message': 'The mail address unavailable'}, 401