import os
import json
import re
from typing import List
import mongomock
import nltk
from nltk.corpus import stopwords
from pymongo import MongoClient
from profanity_filter import ProfanityFilter

mongo_uri = 'mongodb://' + os.environ.get('MONGO_USERNAME') + ':' + os.environ.get('MONGO_PASSWORD') + '@' + os.environ.get('MONGO_HOSTNAME') + ':27017'
test_db = os.environ.get('DB_TEST')

class DBConnect:
    def __init__(self) -> None:
        if test_db == '1':
            self.client = mongomock.MongoClient()
        else:
            self.client = MongoClient(mongo_uri)

    def getCollectionNames(self, database: str) -> List[str]:
        return self.client[database].list_collection_names()
    
    def getDatabaseNames(self) -> List[str]:
        return self.client.list_database_names()

    def getCollectionSize(self, database: str, collection: str) -> int:
        """Returns size of the collection"""
        db = self.client[database]
        cl = db[collection]

        return cl.estimated_document_count()
    
    def getRandomDocument(self, database: str, collection: str) -> dict:
        """Returns a random document from the collection"""
        db = self.client[database]
        cl = db[collection]
        result = cl.aggregate([{"$sample" : { "size" : 1}}])

        for r in result:
            return r

    def writeFileToCollection(self, database: str, collection: str, filename: str) -> None:
        with open(filename, "r", encoding="UTF-8") as file:
            obj = json.load(file)
            data = obj["data"]
            db = self.client[database]
            cl = db[collection]  
            cl.insert_many(data)   

    def writeCollectionToFile(self, database: str, collection: str, filename: str) -> None:
        db = self.client[database]
        cl = db[collection]
        docs = list(cl.find({}))
        file = {}
        file["data"] = docs
        obj = json.dumps(file)

        with open(filename, "w", encoding="UTF-8") as file:
            file.write(obj)

    def censorCollection(self, database: str, collection: str) -> None:
        pf = ProfanityFilter()
        db = self.client[database]
        col = db[collection]

        for document in col.find({}):
            col.update_one(document, {"$set": {"content" : pf.censor(document["content"])}})

    def getDocumentById(self, database: str, collection: str, doc_id: str) -> dict:
        """Returns a document from the collection by querying for an id"""
        db = self.client[database]
        cl = db[collection]
        result = cl.find_one( { "_id": doc_id } ) 
        
        return result
    
    def cleanCollection(self, database: str, collection: str) -> None:
        db = self.client[database]
        cl = db[collection]
        nltk.download("stopwords")

        print("Cleaning...")
        for document in cl.find({}):
            result = document["content"]
            
            # Remove mentions
            result = re.sub("@([a-zA-Z0-9_]{1,50})", "", result)
            # Remove hashtags
            result = re.sub("#([a-zA-Z0-9_]{1,50})", "", result)
            # Remove hyperlinks
            result = re.sub(r"http\S+", "", result)
            # Remove newlines
            result = re.sub("\n", "", result)

            # Remove stop words
            tokens = [word for word in result.split() if word.lower() not in stopwords.words('english')]
            result = " ".join(tokens)

            cl.update_one(document, {"$set": {"content" : result}})
        print("Completed.")

    def closeConnection(self) -> None:
        self.client.close()
