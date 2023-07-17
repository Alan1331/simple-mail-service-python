from flask_restful import Api

from app.resources.registration import Registration
from app.resources.login import Login
from app.resources.logout import Logout
from app.resources.mails import Mails

def register_routes(api: Api):
    api.add_resource(Registration, '/register')
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')
    api.add_resource(Mails, '/mail')