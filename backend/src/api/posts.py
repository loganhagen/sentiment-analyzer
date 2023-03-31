"""API route for handling anything that pertains to tweets"""
import random
from flask import jsonify
from flask_restx import Namespace, Resource
from src.db.connect import DBConnect
from src.lib.languageProcessing import LanguageProcessing

api = Namespace('posts', description='Post related operations')
dbc = DBConnect()

class Tweets(Resource):
    """
    Handles API calls for all tweets.
    """
    def get(self):
        """Get string representation of the Twitter data.."""

        return dbc.getCollectionJSON("UBI", dbc.TWITTER)

    def post(self):
        """Add a new list of tweets."""

class Tweet(Resource):
    """
    Handles single tweet api calls.
    """

    def get(self, tweet_id):
        """Get a tweet by ID."""

    def put(self, tweet_id):
        """Update a tweet by ID."""

    def delete(self, tweet_id):
        """Delete a tweet by ID."""
    
class Reddit(Resource):
    """
    Handles API calls for all Reddit data.
    """
    def get(self):
        """Get a string representation of the Reddit data."""

        return dbc.getCollectionJSON("UBI", dbc.REDDIT)

class Random(Resource):
    """
    Returns a random post.
    """
    def get(self):
        """Get a random post"""
        tweet = dbc.getRandomDocument("UBI", dbc.TWITTER)
        reddit = dbc.getRandomDocument("UBI", dbc.REDDIT)
        tweet_response = jsonify({"text" : str(tweet["content"]), "id": str(tweet["_id"]), "date": str(tweet["created_at"]), "comments": None, "type": "tweet"})
        reddit_response = jsonify({"text" : str(reddit["content"]), "id": str(reddit["_id"]), "date": str(reddit["created_at"]), "comments": reddit["comments"], "type": "reddit"})

        return tweet_response if random.randint(0, 1) == 1 else reddit_response

class SizeAll(Resource):
    """
    Return total number of tweets and reddit posts.
    """
    def get(self):
        """
        Get total number of tweets and reddit posts.
        """
        collection_size = dbc.getCollectionSize("UBI", dbc.TWITTER) + dbc.getCollectionSize("UBI", dbc.REDDIT)
        response = jsonify({"size" : collection_size})

        return response
    
class SizeTweets(Resource):
    """
    Return total number of tweets from database collection.
    """
    def get(self):
        """
        Get total number of tweets from database collection.
        """
        collection_size = dbc.getCollectionSize("UBI", dbc.TWITTER)
        response = jsonify({"size" : collection_size})

        return response
    
class SizeReddit(Resource):
    """
    Return total number of reddit posts.
    """
    def get(self):
        """
        Get total number of reddit posts.
        """
        collection_size = dbc.getCollectionSize("UBI", dbc.REDDIT)
        response = jsonify({"size" : collection_size})

        return response


class Sentiment(Resource):
    """
    Handles sentiment api calls on tweets
    """
    def get(self, post_id:str):
        """
        Get the sentiment of a post by ID
        """
        lp = LanguageProcessing()
        doc = dbc.getDocumentById("UBI", dbc.TWITTER, post_id)
        tweet_text = str(doc["content"])
        sentiment = lp.getSentiment(tweet_text)
        response = jsonify({"Sentiment Analysis": sentiment})

        return response


# Define routes for the API
api.add_resource(Tweets, "/tweets")
api.add_resource(Tweet, "/<string:post_id>")
api.add_resource(Reddit, "/reddit")
api.add_resource(Random, "/random")
api.add_resource(SizeAll, "/size")
api.add_resource(SizeTweets, "/tweets/size")
api.add_resource(SizeReddit, "/reddit/size")
api.add_resource(Sentiment, "/sentiment/<string:post_id>")