from flask import request
from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.datasource_example import user_data
from app.datasource_example import mail_data

class MailsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('type', required=False, location='args')

    @jwt_required()
    def get(self):    
        user_mail_address = get_jwt_identity()
        mail = {}

        args = self.parser.parse_args()
        mail_type = 'all'
        if args['type'] != None:
            mail_type = args['type']

        if mail_type == 'inbox':
            for mail_key, mail_value in mail_data.items():
                if mail_value['receiver'] == user_mail_address:
                    mail[mail_key] = mail_value

        elif mail_type == 'sent':
            for mail_key, mail_value in mail_data.items():
                if mail_value['sender'] == user_mail_address:
                    mail[mail_key] = mail_value

        elif mail_type == 'all':
            for mail_key, mail_value in mail_data.items():
                if (
                    mail_value['receiver'] == user_mail_address
                    or
                    mail_value['sender'] == user_mail_address
                ):
                    mail[mail_key] = mail_value

        return {
            'mail_items': mail,
            'mail_type': mail_type
        }, 200
    
    @jwt_required()
    def post(self):
        user_mail_address = get_jwt_identity()
        receiver = request.form['receiver']
        subject = request.form['subject']
        body = request.form['body']

        if receiver in user_data:
            mail_id = int(max(mail_data.keys()).lstrip('mail')) + 1
            mail_id = 'mail%i' % mail_id

            mail_data[mail_id] = {
                'sender': user_mail_address,
                'receiver': receiver,
                'subject': subject,
                'body': body
            }

            return {
                'message': 'the mail was sent successfully',
                'sent_mail': mail_data[mail_id]
            }, 201
        
        else:
            return {
                'message': 'the receiver mail address is not found',
                'receiver_mail_address': receiver
            }, 400