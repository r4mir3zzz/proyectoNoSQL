import pymongo

def establecer_conexion ():
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = '27017'
    MONGODB_TIMEOUT = 1000
    DATABASE_NAME = 'Proyecto'
    COLLECTION_NAME='app'

    URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"

    try:
        client = pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        client.server_info()
        print ('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))
        return db, collection
        client.close()
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print ('Error with MongoDB connection: %s' % error)
    except pymongo.errors.ConnectionFailure as error:
        print('Could not connect to MongoDB: %s' % error)