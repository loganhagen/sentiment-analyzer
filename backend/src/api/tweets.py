"""API route for handling anything that pertains to tweets"""
import os
from flask import jsonify
from flask_restx import Namespace, Resource
from src.lib.tweetList import TweetList

api = Namespace('tweets', description='Tweet related operations')
t = TweetList(os.environ.get("BEARER_TOKEN"))

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

    def get(self):
        """Get a random tweet"""
        doc = t.getRandomDocument("UBI", "tweets")
        response = jsonify({"tweet" : str(doc["content"])})
        return response

class Size(Resource):
    """
    Returns total amount of tweets in database collection
    """

    def get(self):
        """Get total number of tweets"""
        collection_size = t.getCollectionSize("UBI", "tweets")
        response = jsonify({"size" : collection_size})
        return response

# Define routes for the API
api.add_resource(Tweets, "")
api.add_resource(Tweet, "/<int:tweet_id>")
api.add_resource(RandomTweet, "/random")
api.add_resource(Size, "/size")