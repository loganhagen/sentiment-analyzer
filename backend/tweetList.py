import csv
import json
# from textblob import TextBlob
from datetime import datetime
from pymongo import MongoClient
import pymongo
import tweepy

class TweetList:    
    class Tweet:
        def __init__(self, tweet_id, author_id, created_at, text):
            self.id  = tweet_id
            self.author_id = author_id
            self.created_at = created_at
            self.text = text
            self.polarity = 0.0
            self.subjectivity = 0.0

        def getTweetID(self):
            return self.id

        def getTweetText(self):
            return self.text

        def getTweetPolarity(self):
            return self.polarity

        def getTweetSubjectivity(self):
            return self.subjectivity

        def toString(self):
            return f"tweet_id: {self.id}\nauthor_id: {self.author_id}\ncreated_at: {self.created_at}\ncontent: {self.text}\npolarity: {self.polarity}\nsubjectivity: {self.subjectivity}\n"

        def toList(self):
            return [self.id, self.author_id, self.created_at, self.text, self.polarity, self.subjectivity]

        def toDict(self):
            return {
                "tweet_id" : str(self.id),
                "author_id" : str(self.author_id),
                "created_at" : str(self.created_at),
                "content" : str(self.text)
            }

    def __init__(self, bearer_token):
        self.tweepyClient = tweepy.Client(bearer_token=bearer_token)
        self.mongoClient = MongoClient('mongodb://%s:%s@127.0.0.1' % ("root", "example"))
        self.queryResult = None
        self.tweetList = []

    def getRecentTweets(self, query, limit):
        self.queryResult = tweepy.Paginator(self.tweepyClient.search_recent_tweets, query=query, tweet_fields=['created_at', 'author_id'], max_results=100).flatten(limit=limit)
        self.initTweetList()

    def initTweetList(self):
        for t in self.queryResult:
            # str = self.cleanTweet(t.text)
            self.tweetList.append(self.Tweet(t.id, t.author_id, t.created_at, t.text))

    def getNumTweets(self):
        return len(self.tweetList)

    def printTweetList(self):
        for t in self.tweetList:
            print(t.toString())

    def writeToCSV(self, filename):
        with open(filename, "w", encoding="UTF-8", newline="") as f:
            writer = csv.writer(f)

            for t in self.tweetList:
                writer.writerow(t.toList())

    def readFromCSV(self, filename):
        with open(filename, newline="", encoding="UTF-8") as f:
            reader = csv.reader(f, delimiter=",")

            for r in reader:
                self.tweetList.append(self.Tweet(r[0], r[1], r[2], r[3]))

    def writeToJSON(self, filename):
        fileDict = {
            "date" : str(datetime.now())
        }

        tweetList = []
        for tweet in self.tweetList:        
            tweetList.append(tweet.toDict())

        fileDict["data"] = tweetList
        obj = json.dumps(fileDict)

        with open(filename, "w", encoding="UTF-8") as file:
            file.write(obj)      

    def readFromJSON(self, filename):
        with open(filename, "r", encoding="UTF-8") as f:
            obj = json.load(f)
            data = obj["data"]
            for l in data:
                self.tweetList.append(self.Tweet(l["tweet_id"], l["author_id"], l["created_at"], l["content"]))

    def pushToDB(self, database, collection):
        db = self.mongoClient[database]
        cl = db[collection]
        
        for tweet in self.tweetList:

            obj = {
                "_id" : str(tweet.id),
                "author_id" : str(tweet.author_id),
                "created_at" : str(tweet.created_at),
                "content" : str(tweet.text)
            }

            try:
                cl.insert_one(obj)
            except pymongo.errors.DuplicateKeyError: 
                continue

    def getCollection(self, database, collection, filename):
        db = self.mongoClient[database]
        cl = db[collection]

        output = {
            "date" : str(datetime.now())
        }
        tList = []
        cursor = cl.find({})
        for document in cursor:
            obj = {
                "tweet_id" : str(document["_id"]),
                "author_id" : str(document["author_id"]),
                "created_at" : str(document["created_at"]),
                "content" : str(document["content"])
            }
            tList.append(obj)

        output["data"] = tList

        dictObj = json.dumps(output)

        with open(filename, 'w', encoding='UTF-8') as file:  
            file.write(dictObj)

    def getCollectionSize(self, database, collection):
        db = self.mongoClient[database]
        cl = db[collection]

        return cl.estimated_document_count()

    def getRandomDocument(self, database, collection):
        db = self.mongoClient[database]
        cl = db[collection]
        result = cl.aggregate([{"$sample" : { "size" : 1}}])

        for r in result:
            return r