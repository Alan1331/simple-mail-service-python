# Load the .env file
import os
from dotenv import load_dotenv
load_dotenv()

url = 'http://' + os.environ.get('MAIL_SERVICE_ADD')

import requests

from app.utils.cache import if_cache_hit, cache_result

class Mail:
    def create_mail(mail):
        # Create a new mail document in the collection
        endpoint = '/api/mails'
        response = requests.post(url + endpoint, json=mail)

        if response.status_code == 201:
            return 'success'
        
        if response.status_code == 500:
            return 'db_error'

    def get_all_mails(mail_address, type):
        # Retrieve all mail related to given mail_address from the mail api
        endpoint = '/api/mails'
        querystring = {
            'mail-address': mail_address
        }

        if type != 'all':
            querystring['type'] = type

        # complete_url is including querystring
        complete_url = url + endpoint + '?mail-address=' + querystring['mail-address']

        cache_hit = if_cache_hit(complete_url)
        if cache_hit != None:
            return cache_hit

        print("sending api request to mail-api")
        response = requests.get(url + endpoint, params=querystring)

        if response.status_code == 200:
            response_dict = response.json()
            result = response_dict['result']

            # cache the result
            cache_result(
                key=complete_url,
                result=result
            )

            return result
        
        if response.status_code == 400:
            return 'invalid_params'

    def get_mail_by_id(mail_id):
        # Retrieve a single mail based on the given ID
        endpoint = '/api/mails/' + mail_id
        complete_url = url + endpoint

        cache_hit = if_cache_hit(complete_url)
        if cache_hit != None:
            return cache_hit

        print("sending api request to mail-api")
        response = requests.get(complete_url)

        if response.status_code == 200:
            response_dict = response.json()
            result = response_dict['result']

            # cache the result
            cache_result(
                key=complete_url,
                result=result
            )

            return result
        
        if response.status_code == 404:
            return None

    def delete_mail(mail_id):
        # Delete the mail based on given ID
        endpoint = '/api/mails/' + mail_id
        response = requests.delete(url + endpoint)

        if response.status_code == 200:
            return 'success'
        
        if response.status_code == 404:
            return 'not_found'
        
        if response.status_code == 500:
            return 'db_error'
