from app.config import development
from flask import Flask
from flask_restful import Api

from app.jwt_config import jwt
from app.routes import register_routes

app = Flask(__name__)
app.config.from_object(development.DevelopmentConfig)

# Initialize JWT with the app
jwt.init_app(app)

# Initialize API and register all routes
api = Api(app)
register_routes(api=api)