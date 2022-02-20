import pymongo

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MongoConnection(metaclass=SingletonMeta):

    def __init__(self):
        self.database_name = 'parspooyeshDB'
        self.port = '27017'
        self.connection_string = f"mongodb://localhost:{self.port}"
        self.my_client = self.__connection(self.connection_string)
        self.my_db = self.my_client[self.database_name]
        print('call connection one ++++++++++++++++++++++')
    
    def __connection(self, connection_sting):
        return  pymongo.MongoClient(connection_sting)
    
    def find(self, collection_name, conditions):
        my_collections = self.my_db[collection_name]
        return my_collections.find(conditions)
