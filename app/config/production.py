import os
from dotenv import load_dotenv
from datetime import timedelta

# Load the .env file
load_dotenv()

class ProductionConfig:
    DEBUG = False

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)

    DATABASE_URL = os.environ.get('DATABASE_URL')