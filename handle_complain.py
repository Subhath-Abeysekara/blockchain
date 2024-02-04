from service.connection import connect_mongo_complain

collection_name = connect_mongo_complain()
#
# collections_ = list(collection_name.find())
# print(collections_)

def set_doc(doc):
    del doc['_id']
    return doc

def set_docs(docs):
    return list(map(lambda doc:set_doc(doc),docs))

def add_complain(complain):
    collection_name.insert_one(complain)
    return {
        "state":True
    }

def get_complain_by_user(private_key):
    collections_ = collection_name.find({'private_key':private_key})
    return set_docs(collections_)

def get_complain_by_reviewer(reviewer_id):
    collections_ = collection_name.find({'reviewer_id':reviewer_id})
    return set_docs(collections_)

def get_complain_by_admin():
    collections_ = collection_name.find({'reviewer_id':""})
    return set_docs(collections_)

def add_reviewer(id , reviewer_id):
    collection_name.update_one({'id':int(id)},{'$set':{'reviewer_id':reviewer_id}})
    return {
        "state":True
    }




