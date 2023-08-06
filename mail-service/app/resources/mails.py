from flask import request
from flask_restful import reqparse, Resource

from app.models.mails import Mail
from app.models.users import User

class MailsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('mail-address', required=True, location='args')
        self.parser.add_argument('type', required=False, location='args')

    def get(self):    
        args = self.parser.parse_args()
        user_mail_address = args['mail-address']

        result = None

        mail_type = 'all'
        if args['type'] != None:
            mail_type = args['type']

        if mail_type == 'inbox':
            result = Mail.get_inbox_mails(user_mail_address)

        elif mail_type == 'sent':
            result = Mail.get_sent_mails(user_mail_address)

        elif mail_type == 'all':
            result = Mail.get_all_mails()

        return {
            'message': 'Requested mails were successfully received',
            'result': result
        }, 200
    
    def post(self):
        data = request.get_json()

        sender = data.get('sender')
        receiver = data.get('receiver')
        subject = data.get('subject')
        body = data.get('body')

        if sender == None or receiver == None or subject == None or body == None :
            return {"message": "Invalid JSON data in the request body"}, 400
        
        is_sender_add_avail = User.get_user_by_mail_address(sender) != None
        is_receiver_add_avail = User.get_user_by_mail_address(receiver) != None

        if is_sender_add_avail and is_receiver_add_avail:

            mail_data = {
                'sender': sender,
                'receiver': receiver,
                'subject': subject,
                'body': body
            }

            result = Mail.create_mail(mail=mail_data)

            # If the email was written successfully to the database
            if result['acknowledged'] == True:
                return {
                    'message': 'The mail was sent successfully'
                }, 201
            # If the email was not written successfully to the database
            else:
                return {
                    'message': 'Failed to send the mail due to database error'
                }, 500
        
        else:
            return {
                'message': 'The sender or receiver mail address is not found'
            }, 400