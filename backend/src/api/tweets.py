"""API route for handling anything that pertains to tweets"""
from flask import jsonify
from flask_restx import Namespace, Resource
from src.db.connect import DBConnect
from src.lib.twitter import Twitter
from src.lib.languageProcessing import LanguageProcessing

api = Namespace('tweets', description='Tweet related operations')

class Tweets(Resource):
    """
    Handles API calls for all tweets
    """
    def get(self):
        """Get a list of tweets"""
        tweets = {
            "data": [{
                "_id": "1623133583446806529",
                "author_id": "1942422685",
                "created_at": "2023-02-08 01:36:17+00:00",
                "content": "@MarioNawfal @AndrewYang #ChatGPT founder says AI will require a Universal Basic Income \n\nSam Altman says it should be paid out via cryptocurrency &amp; funded in part by the increased GDP created by AI https://t.co/ULUYQB3d2V"
            }, {
                "_id": "1623131251761885190",
                "author_id": "1595075622899896320",
                "created_at": "2023-02-08 01:27:01+00:00",
                "content": "@MarioNawfal @AndrewYang \n\nHow you going to deal with crazy men?  \n\nUniversal basic income?  \n\nI think that's the main idea getting thrown around right now."
            }, {
                "_id": "1623131235072761856",
                "author_id": "1405111330072268802",
                "created_at": "2023-02-08 01:26:57+00:00",
                "content": "@MilesKlee I did it.  Brian Krassenstein asked Andrew yang 'is chatGPT going to make universal basic income more necessary?\"\n\nAnd then I got out."
            }]
        }

        dbc = DBConnect()
        return jsonify(dbc.getCollectionJSON("UBI", "tweets"))

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
        dbc = DBConnect()
        doc = dbc.getRandomDocument("UBI", "tweets")
        response = jsonify({"text" : str(doc["content"]), "id": str(doc["_id"]), "date": str(doc["created_at"]), "type": "tweet"})
        dbc.closeConnection()

        return response

class Size(Resource):
    """
    Returns total amount of tweets in database collection
    """
    def get(self):
        """
        Get total number of tweets from database collection
        """
        dbc = DBConnect()
        collection_size = dbc.getCollectionSize("UBI", "tweets")
        response = jsonify({"size" : collection_size})
        dbc.closeConnection()

        return response


class Sentiment(Resource):
    """
    Handles sentiment api calls on tweets
    """
    def get(self, post_id:str):
        """
        Get the sentiment of a post by ID
        """
        dbc = DBConnect()
        lp = LanguageProcessing()
        doc = dbc.getDocumentById("UBI", "tweets", post_id)
        tweet_text = str(doc["content"])
        sentiment = lp.getSentiment(tweet_text)
        response = jsonify({"Sentiment Analysis": sentiment})
        dbc.closeConnection()

        return response


# Define routes for the API
api.add_resource(Tweets, "")
api.add_resource(Tweet, "/<string:post_id>")
api.add_resource(RandomTweet, "/random")
api.add_resource(Size, "/size")
api.add_resource(Sentiment, "/sentiment/<string:post_id>")