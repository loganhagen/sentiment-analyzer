"""Class that handles tweets for our backend API"""
import os
import csv
import json
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pymongo
import tweepy
import mongomock
# from textblob import TextBlob

mongo_uri = 'mongodb://' + os.environ.get('MONGO_USERNAME') + ':' + os.environ.get('MONGO_PASSWORD') + '@' + os.environ.get('MONGO_HOSTNAME') + ':27017'
test_db = os.environ.get('TEST_DB')
print(test_db)

class TweetList:
    """Class that handles tweets for our backend API"""    
    def __init__(self):
        self.tweepy_client = tweepy.Client(os.environ.get("BEARER_TOKEN"))
        self.mongo_client = None

        if test_db == '1':
            self.mongo_client = mongomock.MongoClient()
        elif test_db == '0':
            pass
            # self.mongo_client = MongoClient(mongo_uri)
        
        self.query_result = None
        self.tweet_list = []

    def getTweepyBearerToken(self):
        return self.tweepy_client.bearer_token

    def getMongoClientStatus(self):
        try:
            self.mongo_client.admin.command('ismaster')
        except ConnectionFailure:
            return "Server not available"
        return "Server available"

    def getRecentTweets(self, query, limit):
        """Returns a list of recent tweets"""
        self.query_result = tweepy.Paginator(
            self.tweepy_client.search_recent_tweets,
            query=query,
            tweet_fields=['created_at', 'author_id'],
            max_results=100
        ).flatten(limit=limit)

        self.initTweetList()

    def initTweetList(self):
        """Initializes the tweet list"""
        for tweet in self.query_result:
            self.tweet_list.append(
                self.Tweet(
                    tweet.id,
                    tweet.author_id,
                    tweet.created_at,
                    tweet.text
                )
            )

    def emptyList(self):
        self.tweet_list.clear()
        
    def getNumTweets(self):
        """Returns the number of tweets"""
        return len(self.tweet_list)

    def printTweetList(self):
        """Prints the tweet list"""
        for tweet in self.tweet_list:
            print(tweet.toString())

    def writeToCSV(self, filename):
        """Writes the tweet list to a CSV file"""
        with open(filename, "w", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)

            for tweet in self.tweet_list:
                writer.writerow(tweet.toList())

    def readFromCSV(self, filename):
        """Reads the tweet list from a CSV file"""
        with open(filename, newline="", encoding="UTF-8") as file:
            reader = csv.reader(file, delimiter=",")

            for row in reader:
                self.tweet_list.append(self.Tweet(row[0], row[1], row[2], row[3]))

    def writeToJSON(self, filename):
        """Writes the tweet list to a JSON file"""
        file_dict = {
            "date" : str(datetime.now())
        }

        tweet_list = []
        for tweet in self.tweet_list:      
            tweet_list.append(tweet.toDict())

        file_dict["data"] = tweet_list
        obj = json.dumps(file_dict)

        with open(filename, "w", encoding="UTF-8") as file:
            file.write(obj)

    def readFromJSON(self, filename):
        """Reads the tweet list from a JSON file"""
        with open(filename, "r", encoding="UTF-8") as file:
            obj = json.load(file)
            data = obj["data"]
            for l in data:
                self.tweet_list.append(
                    self.Tweet(l["tweet_id"],
                    l["author_id"],
                    l["created_at"],
                    l["content"])
                )

    # This is a very slow function.
    def pushToDB(self, database, collection):
        """Pushes the tweet list to the database"""
        db = self.mongo_client[database]
        cl = db[collection]       
        for tweet in self.tweet_list:

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

    def writeCollectionToJSON(self, database, collection, filename):
        """Returns a collection from the database"""
        db = self.mongo_client[database]
        cl = db[collection]
        output = {"date" : str(datetime.now())}
        t_list = []
        cursor = cl.find({})
        for document in cursor:
            obj = {
                "tweet_id" : str(document["_id"]),
                "author_id" : str(document["author_id"]),
                "created_at" : str(document["created_at"]),
                "content" : str(document["content"])
            }
            t_list.append(obj)

        output["data"] = t_list

        dict_obj = json.dumps(output)

        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(dict_obj)

    def getCollectionSize(self, database, collection):
        """Returns size of the collection"""
        db = self.mongo_client[database]
        cl = db[collection]

        return cl.estimated_document_count()

    def getRandomDocument(self, database, collection):
        """Returns a random document from the collection"""
        db = self.mongo_client[database]
        cl = db[collection]
        result = cl.aggregate([{"$sample" : { "size" : 1}}])

        for r in result:
            return r

    class Tweet:
        """Class that represents a tweet as a data type"""
        def __init__(self, tweet_id, author_id, created_at, text):
            self.id  = tweet_id
            self.author_id = author_id
            self.created_at = created_at
            self.text = text
            self.polarity = 0.0
            self.subjectivity = 0.0

        def getTweetID(self):
            """Returns the tweet id"""
            return self.id

        def getTweetText(self):
            """Returns the tweet text"""
            return self.text

        def getTweetPolarity(self):
            """Returns the polarity of the tweet"""
            return self.polarity

        def getTweetSubjectivity(self):
            """Returns the subjectivity of the tweet"""
            return self.subjectivity

        def toString(self):
            """Returns a string representation of the tweet"""
            return f"tweet_id: {self.id}\nauthor_id: {self.author_id}\ncreated_at: {self.created_at}\ncontent: {self.text}\npolarity: {self.polarity}\nsubjectivity: {self.subjectivity}\n"

        def toList(self):
            """Returns a list representation of the tweet"""
            return [self.id, self.author_id, self.created_at, self.text, self.polarity, self.subjectivity]

        def toDict(self):
            """Returns a dictionary representation of the tweet"""
            return {
                "tweet_id" : str(self.id),
                "author_id" : str(self.author_id),
                "created_at" : str(self.created_at),
                "content" : str(self.text)
            }
