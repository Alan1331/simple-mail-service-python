import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class DevelopmentConfig:
    DEBUG = True

    MAIL_DB_URL = os.environ.get('MAIL_DB_URL')