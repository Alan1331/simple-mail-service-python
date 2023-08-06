from bson import ObjectId

from app import db
from app.utils.parser import parse_received_collection
from app.utils.parser import parse_received_document

class Mail:
    def create_mail(mail):
        # Create a new mail document in the collection
        raw_result = db.mail.insert_one(mail)

        # Convert result from InsertOneResult object to dictionary
        # and convert the inserted_id to str
        result = {
            'acknowledged': raw_result.acknowledged,
            'inserted_id': str(raw_result.inserted_id)
        }

        return result

    def get_inbox_mails(user_mail_address):
        # Retrieve received mail documents from the collection
        result = db.mail.find({"receiver": user_mail_address})
        return parse_received_collection(result)

    def get_sent_mails(user_mail_address):
        # Retrieve sent mail documents from the collection
        result = db.mail.find({"sender": user_mail_address})
        return parse_received_collection(result)

    def get_all_mails():
        # Retrieve all mail documents from the collection
        result = db.mail.find()
        return parse_received_collection(result)

    def get_mail_by_id(mail_id):
        # Retrieve a single mail document based on the provided ID
        result = db.mail.find_one({'_id': ObjectId(mail_id)})

        if result != None:
            return parse_received_document(result)
        else:
            return result

    def update_mail(mail_id, updated_data):
        # Update the mail document with the provided ID
        db.mail.update_one({'_id': mail_id}, {'$set': updated_data})

    def delete_mail(mail_id):
        # Delete the mail document with the provided ID
        return db.mail.delete_one({'_id': ObjectId(mail_id)})
