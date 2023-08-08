import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

from app import app

if __name__ == '__main__':
    app.run(ost=(os.environ.get('CORE_SERVICE_ADD')))