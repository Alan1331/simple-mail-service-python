from flask import request
from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.mails import Mail
from app.models.users import User

class MailsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('type', required=False, location='args')

    @jwt_required()
    def get(self):    
        user_mail_address = get_jwt_identity()
        result = None

        args = self.parser.parse_args()
        mail_type = 'all'
        if args['type'] != None:
            mail_type = args['type']

        result = Mail.get_all_mails(user_mail_address, mail_type)

        if result == 'invalid_params':
            return {
                'message': 'Parameter code error on server'
            }, 500
        
        return {
            'message': 'Requested mails were successfully received',
            'result': result
        }, 200
    
    @jwt_required()
    def post(self):
        user_mail_address = get_jwt_identity()
        receiver = request.form['receiver']
        subject = request.form['subject']
        body = request.form['body']

        is_receiver_add_avail = User.get_user_by_mail_address(user_mail_address=receiver)

        if is_receiver_add_avail != None:

            mail_data = {
                'sender': user_mail_address,
                'receiver': receiver,
                'subject': subject,
                'body': body
            }

            result = Mail.create_mail(mail=mail_data)

            # If the email was written successfully to the database
            if result == 'success':
                return {
                    'message': 'The mail was sent successfully'
                }, 201
            
            # If the email was not written successfully to the database
            if result == 'db_error':
                return {
                    'message': 'The mail could not be sent to the database due to database error'
                }, 500
        
        else:
            return {
                'message': 'The receiver mail address is not found'
            }, 400