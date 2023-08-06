import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class ProductionConfig:
    DEBUG = False

    USER_DB_URL = os.environ.get('USER_DB_URL')