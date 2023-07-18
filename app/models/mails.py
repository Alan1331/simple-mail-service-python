# app/models/mail_model.py
from pymongo import MongoClient

class Mails:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # Update connection details if needed
        self.db = self.client['mail_app_db']
        self.collection = self.db['mails']

    def create_mail(self, mail_data):
        # Create a new mail document in the collection
        self.collection.insert_one(mail_data)

    def get_all_mails(self):
        # Retrieve all mail documents from the collection
        return list(self.collection.find())

    def get_mail_by_id(self, mail_id):
        # Retrieve a single mail document based on the provided ID
        return self.collection.find_one({'_id': mail_id})

    def update_mail(self, mail_id, updated_data):
        # Update the mail document with the provided ID
        self.collection.update_one({'_id': mail_id}, {'$set': updated_data})

    def delete_mail(self, mail_id):
        # Delete the mail document with the provided ID
        self.collection.delete_one({'_id': mail_id})
