from pymongo import MongoClient

class DatabaseClient():
    def __init__(self, client_connection):
        self.client = MongoClient(client_connection)
        self.collection = self.client.iot
    
    def save_data(self, line):
        
        inserted_data = self.collection.data
        inserted_data.insert_one(line)

        return True