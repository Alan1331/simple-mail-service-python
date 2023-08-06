# Parse received collection from db to convert _id to str
def parse_received_collection(collection):
    collection = list(collection)

    for document in collection:
        document['_id'] = str(document['_id'])

    return collection

# Parse received single document from db to convert _id to str
def parse_received_document(document):
    document['_id'] = str(document['_id'])

    return document