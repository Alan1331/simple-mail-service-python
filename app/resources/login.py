from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from app.datasource_example import user_data

class LoginResource(Resource):
    def post(self):
        mail_address = request.form['mail_address']
        input_password = request.form['password']
        
        if mail_address in user_data:
            stored_password = user_data[mail_address]['password']

            if input_password == stored_password:
                access_token = create_access_token(identity=mail_address)
                return {
                    'message': 'User logged in successfully',
                    'access_token': access_token
                }, 200
            else:
                return {'message': 'wrong password'}, 401
        
        else:
            return {'message': 'mail address unavailable'}, 401