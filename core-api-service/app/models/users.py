# Load the .env file
import os
from dotenv import load_dotenv
load_dotenv()

url = 'http://' + os.environ.get('USER_SERVICE_ADD')

import requests

from app.utils.cache import if_cache_hit, cache_result

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
        complete_url = url + endpoint

        cache_hit = if_cache_hit(complete_url)
        if cache_hit != None:
            return cache_hit

        print("sending api request to user-api")

        response = requests.get(complete_url)

        if response.status_code == 404:
            return None
        
        if response.status_code == 200:
            response_dict = response.json()
            result = response_dict['result']

            # cache the result
            cache_result(
                key=complete_url,
                result=result
            )

            return result