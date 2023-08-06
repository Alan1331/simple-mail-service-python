from app import db
from app.utils.parser import parse_received_document

class User:
    def create_user(user):
        # Create a new user document in the collection
        result = db.user.insert_one(user)
        return result

    def get_all_user():
        # Retrieve all user documents from the collection
        return list(db.user.find())

    def get_user_by_id(user_id):
        # Retrieve a single user document based on the provided ID
        return db.user.find_one({'_id': user_id})

    def get_user_by_mail_address(user_mail_address):
        # Retrieve a single user document based on the provided user mail address
        result = db.user.find_one({'mail_address': user_mail_address})

        if result != None:
            result = parse_received_document(result)

        return result

    def update_user(user_mail_address, updated_data):
        # Update the user document with the provided user mail address
        result = db.user.update_one(
            {'mail_address': user_mail_address},
            {'$set': updated_data}
        )
        return result

    def delete_user(user_mail_address):
        # Delete the user document with the provided user mail address
        result = db.user.delete_one({'mail_address': user_mail_address})
        return result