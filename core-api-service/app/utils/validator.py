# Validate given mongodb id
from bson import ObjectId

def validate_mail_id(function):
    def wrapper(self, mail_id):
        
        if ObjectId.is_valid(mail_id):
            return function(self, mail_id)
        else:
            return {'message': 'Invalid mail id'}, 400

    return wrapper