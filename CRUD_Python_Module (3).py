# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://localhost:27017')
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
        # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        try:
            data = self.database.animals.find(query, {"_id": False})
            return list(data)
        except Exception as e:
            print("Error reading data:", e)
            return []
         # Create method to implement the U in CRUD.
    def update(self, query, newData):
        try:
            result = self.database.animals.update_many(
                query,
                {"$set": newData}
            )
            return result.modified_count
        except Exception as e:
            print("Error updating data:", e)
            return 0


    # Create method to implement the D in CRUD.
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Error deleting data:", e)
            return 0