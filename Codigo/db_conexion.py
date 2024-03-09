import pymongo

# Función para establecer conexión a la base de datos MongoDB para una colección específica
def establecer_conexion(collection_name):
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = '27017'
    MONGODB_TIMEOUT = 1000
    DATABASE_NAME = 'Proyecto'

    URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"

    try:
        client = pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT)
        db = client[DATABASE_NAME]
        collection = db[collection_name]
        client.server_info()
        print ('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))
        return db, collection
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print ('Error with MongoDB connection: %s' % error)
    except pymongo.errors.ConnectionFailure as error:
        print('Could not connect to MongoDB: %s' % error)