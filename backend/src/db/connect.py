import os
import json
import mongomock
from pymongo import MongoClient
from profanity_filter import ProfanityFilter

mongo_uri = 'mongodb://' + os.environ.get('MONGO_USERNAME') + ':' + os.environ.get('MONGO_PASSWORD') + '@' + os.environ.get('MONGO_HOSTNAME') + ':27017'
test_db = os.environ.get('DB_TEST')

class DBConnect:
    def __init__(self):
        if test_db == '1':
            self.client = mongomock.MongoClient()
        else:
            self.client = MongoClient(mongo_uri)

    def getCollectionSize(self, database, collection) -> int:
        """Returns size of the collection"""
        db = self.client[database]
        cl = db[collection]

        return cl.estimated_document_count()
    
    def getRandomDocument(self, database, collection):
        """Returns a random document from the collection"""
        db = self.client[database]
        cl = db[collection]
        result = cl.aggregate([{"$sample" : { "size" : 1}}])

        for r in result:
            return r

    def writeFileToCollection(self, database, collection, filename):
        with open(filename, "r", encoding="UTF-8") as file:
            obj = json.load(file)
            data = obj["data"]
            db = self.client[database]
            cl = db[collection]  
            cl.insert_many(data)   

    def writeCollectionToFile(self, database, collection, filename):
        db = self.client[database]
        cl = db[collection]
        docs = list(cl.find({}))
        file = {}
        file["data"] = docs
        obj = json.dumps(file)

        with open(filename, "w", encoding="UTF-8") as file:
            file.write(obj)

    def censorCollection(self, database, collection):
        pf = ProfanityFilter()
        db = self.client[database]
        col = db[collection]

        for document in col.find({}):
            col.update_one(document, {"$set": {"content" : pf.censor(document["content"])}})

    def getDocumentById(self, database, collection, tweet_id):
        """Returns a document from the collection by querying for an id"""
        db = self.client[database]
        cl = db[collection]
        result = cl.find_one( { "_id": tweet_id } ) 
        
        return result
