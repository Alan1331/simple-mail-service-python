from flask_restful import Api

from app.resources.mails import MailsResource
from app.resources.mail import SingleMailResource

def register_routes(api: Api):
    api.add_resource(MailsResource, '/api/mails')
    api.add_resource(SingleMailResource, '/api/mails/<string:mail_id>')