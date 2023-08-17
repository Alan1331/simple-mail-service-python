# Load the .env file
import os
from dotenv import load_dotenv
load_dotenv()

url = 'http://' + os.environ.get('USER_SERVICE_ADD')

import requests

class User:
    def create_user(user):
        # Create a new user
        endpoint = '/api/users'
        response = requests.post(url + endpoint, json=user)

        if response.status_code == 201:
            return 'success'
        
        if response.status_code == 500:
            return 'db_error'

    def get_user_by_mail_address(user_mail_address):
        # Retrieve a single user based on the provided user mail address
        endpoint = '/api/users/' + user_mail_address
        response = requests.get(url + endpoint)

        if response.status_code == 404:
            return None
        
        if response.status_code == 200:
            response_dict = response.json()
            result = response_dict['result']
            return result