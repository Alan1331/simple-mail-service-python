from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from app.datasource_example import user_data

class RegistrationResource(Resource):
    def post(self):
        # get registration data from client's form
        mail_address = request.form['mail_address']
        password = request.form['password']
        confirmation_password = request.form['confirmation_password']

        # Check if the confirmation password is correct
        if password != confirmation_password:
            return {'message': 'your confirmation password is wrong'}, 400

        # Check if the user already exists in the database
        if mail_address in user_data:
            return {'message': 'the mail address was registered'}, 400
        # If not, create a new user
        else:
            # Store the user's username and hashed password in the database
            user_data[mail_address] = {'password': password}
            access_token = create_access_token(identity=mail_address)
            return {
                'message': 'User registered successfully',
                'access_token': access_token
            }, 201