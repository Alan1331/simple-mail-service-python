from flask import request
from flask_restful import reqparse, Resource

from app.models.users import User

class UsersResource(Resource):    
    def post(self):
        # get registration data from json request body
        data = request.get_json()

        mail_address = data.get('mail_address')
        password = data.get('password')
        
        # Store the user's mail address and hashed password in the database
        new_user = {
            'mail_address': mail_address,
            'password': password
        }
        result = User.create_user(new_user)

        # If user data is successfully written to the database
        if result.acknowledged == True:
            return {
                'message': 'User account was successfully stored'
            }, 201
        # If user data is not written to the database
        else:
            return {
                'message': 'Failed to store user data due to database error'
            }, 500
                