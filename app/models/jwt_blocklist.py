from pymongo import MongoClient

from app import db

class JwtBlocklist:
    def add_token(jwt_token):
        # Add jwt token document to the collection
        result = db.jwt_blocklist.insert_one(jwt_token)
        return result

    def get_token(jwt_token):
        # Retrieve a single token document based on the provided token
        return db.jwt_blocklist.find_one({'token': jwt_token})