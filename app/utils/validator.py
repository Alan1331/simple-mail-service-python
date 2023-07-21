# Validate given mongodb id
from bson import ObjectId

def is_valid_object_id(string_id):
    return ObjectId.is_valid(string_id)