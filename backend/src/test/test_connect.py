import json
import pytest
import mongomock

@pytest.fixture
def db():
    return mongomock.MongoClient()

def test_writeCollection(db):
    with open("test_tweets.json", "r", encoding="UTF-8") as file:
        obj = json.load(file)
        data = obj["data"]
        db = db["UBI"]
        cl = db["tweets"]  
        cl.insert_many(data, ordered=False)  

    assert cl.estimated_document_count() == 3393

def test_getDocumentByID(db):
    with open("test_tweets.json", "r", encoding="UTF-8") as file:
        obj = json.load(file)
        data = obj["data"]
        db = db["UBI"]
        cl = db["tweets"]  
        cl.insert_many(data, ordered=False)  
        result = cl.find_one({"_id": "1623133583446806529"}) 

        assert result is not None

def test_getRandomDocument(db):
    with open("test_tweets.json", "r", encoding="UTF-8") as file:
        obj = json.load(file)
        data = obj["data"]
        db = db["UBI"]
        cl = db["tweets"]  
        cl.insert_many(data, ordered=False)
        doc = list(cl.aggregate([{"$sample" : { "size" : 1}}]))

        assert doc is not None
