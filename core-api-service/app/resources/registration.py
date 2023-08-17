from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from app.models.users import User

class RegistrationResource(Resource):
    def post(self):
        # get registration data from client's form
        mail_address = request.form['mail_address']
        password = request.form['password']
        confirmation_password = request.form['confirmation_password']

        # Check if the confirmation password is correct
        if password != confirmation_password:
            return {'message': 'Your confirmation password is wrong'}, 400
        
        # Check if the user already exists in the database
        is_user_avail = User.get_user_by_mail_address(user_mail_address=mail_address)
        if is_user_avail != None:
            return {'message': 'The mail address was already registered'}, 400
        
        # If not, create a new user
        else:
            # Store the user's mail address and hashed password in the database
            new_user = {
                'mail_address': mail_address,
                'password': password
            }
            result = User.create_user(new_user)

            # If user data was not written to the database
            if result == 'db_error':
                return {
                    'message': 'Failed to store user data due to database error'
                }, 500

            # If user data was written to the database
            if result == 'success':
                access_token = create_access_token(identity=mail_address)
                return {
                    'message': 'User registered successfully',
                    'access_token': access_token
                }, 201

                