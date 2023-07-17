from app.config import development
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta

from app.datasource_example import blocklist
from app.routes import register_routes

app = Flask(__name__)
app.config.from_object(development.DevelopmentConfig)

ACCESS_EXPIRES = timedelta(minutes=30)

app.config['JWT_SECRET_KEY'] = 'simplemailappbymr1331'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload['jti']
    token_in_blocklist = jti in blocklist
    return token_in_blocklist

api = Api(app)

register_routes(api=api)