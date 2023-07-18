from flask_restful import Api

from app.resources.registration import RegistrationResource
from app.resources.login import LoginResource
from app.resources.logout import LogoutResource
from app.resources.mails import MailsResource

def register_routes(api: Api):
    api.add_resource(RegistrationResource, '/register')
    api.add_resource(LoginResource, '/login')
    api.add_resource(LogoutResource, '/logout')
    api.add_resource(MailsResource, '/mail')