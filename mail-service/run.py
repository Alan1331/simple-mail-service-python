import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

from app import app

if __name__ == '__main__':
    app.run(host=(os.environ.get('MAIL_SERVICE_ADD')))