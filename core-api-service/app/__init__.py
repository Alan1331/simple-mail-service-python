# Load the .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize db connection and get the required database
from pymongo import MongoClient

db_conn = MongoClient(os.environ.get('CORE_DB_URL'))
db = db_conn['core-db']

# Initialize flask app
from flask import Flask
app = Flask(__name__)

# Load environment config
from app.config import development
from app.config import production

FLASK_ENV = os.environ.get('FLASK_ENV')
if FLASK_ENV == 'production':
    app.config.from_object(production.ProductionConfig)
else:
    app.config.from_object(development.DevelopmentConfig)

# Initialize JWT with the app
from app.jwt_config import jwt
jwt.init_app(app)

# Initialize API and register all routes
from flask_restful import Api
api = Api(app)
from app.routes import register_routes
register_routes(api=api)