import pymongo

# database 연결
def connect_database(db):
    connect_to = pymongo.MongoClient("mongodb://wkdso0804:<bewhy0691>@cluster0.2ix2w.mongodb.net/?retryWrites=true&w=majority")
    mdb = connect_to[db]
    return mdb

# collection 연결
def use(db, collection):
    return db[collection]

def insert(collection, data_list):
    collection.insert_many(data_list)

def find(collection, options = {}):
    searched = collection.find(options)
    return searched

def update(collection, options = {}):
    collection.update_many(options)

def delete(collection, options = {}):
    collection.delete_many(options)