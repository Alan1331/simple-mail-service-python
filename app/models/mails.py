from pymongo import MongoClient

from app import db

class Mail:
    def create_mail(mail):
        # Create a new mail document in the collection
        result = db.mail.insert_one(mail)
        return result

    def get_inbox_mails(user_mail_address):
        # Retrieve received mail documents from the collection
        return list(db.mail.find({"receiver": user_mail_address}))

    def get_sent_mails(user_mail_address):
        # Retrieve sent mail documents from the collection
        return list(db.mail.find({"sender": user_mail_address}))

    def get_all_mails():
        # Retrieve all mail documents from the collection
        return list(db.mail.find())

    def get_mail_by_id(mail_id):
        # Retrieve a single mail document based on the provided ID
        return db.mail.find_one({'_id': mail_id})

    def update_mail(mail_id, updated_data):
        # Update the mail document with the provided ID
        db.mail.update_one({'_id': mail_id}, {'$set': updated_data})

    def delete_mail(mail_id):
        # Delete the mail document with the provided ID
        db.mail.delete_one({'_id': mail_id})
