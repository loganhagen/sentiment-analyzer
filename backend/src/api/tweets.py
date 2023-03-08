"""API route for handling anything that pertains to tweets"""
from flask import jsonify
from flask_restx import Namespace, Resource
from src.db.connect import DBConnect
from src.lib.languageProcessing import LanguageProcessing
from flask_cors import cross_origin

api = Namespace('tweets', description='Tweet related operations')
dbc = DBConnect()

class Tweets(Resource):
    """
    Handles API calls for all tweets
    """
    def get(self):
        """Get a list of tweets"""

    def post(self):
        """Add a new list of tweets"""

class Tweet(Resource):
    """
    Handles single tweet api calls
    """

    def get(self, tweet_id):
        """Get a tweet by ID"""

    def put(self, tweet_id):
        """Update a tweet by ID"""

    def delete(self, tweet_id):
        """Delete a tweet by ID"""


class RandomTweet(Resource):
    """
    Returns a random tweet
    """
    @cross_origin()
    def get(self):
        """Get a random tweet"""
        doc = dbc.getRandomDocument("UBI", "tweets")
        response = jsonify({"tweet" : str(doc["content"]), "id": str(doc["_id"])})

        return response

class Size(Resource):
    """
    Returns total amount of tweets in database collection
    """
    @cross_origin()
    def get(self):
        """
        Get total number of tweets from database collection
        """
        collection_size = dbc.getCollectionSize("UBI", "tweets")
        response = jsonify({"size" : collection_size})
        return response


class Sentiment(Resource):
    """
    Handles sentiment api calls on tweets
    """
    @cross_origin()
    def get(self, tweet_id:str):
        """
        Get the sentiment of a tweet by ID
        """
        lp = LanguageProcessing()
        doc = dbc.getDocumentById("UBI", "tweets", tweet_id)
        tweet_text = str(doc["content"])
        sentiment = lp.getSentiment(tweet_text)
        response = jsonify({"Sentiment Analysis": sentiment})

        return response


# Define routes for the API
api.add_resource(Tweets, "")
api.add_resource(Tweet, "/<string:tweet_id>")
api.add_resource(RandomTweet, "/random")
api.add_resource(Size, "/size")
api.add_resource(Sentiment, "/sentiment/<string:tweet_id>")