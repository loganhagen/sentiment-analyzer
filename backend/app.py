"""app.py"""

import os
import tweetList
from flask import Flask
import flask

app = Flask(__name__)

t = tweetList.TweetList(os.environ.get("BEARER_TOKEN"))

@app.route("/")
def hello_world():
    """hello_world"""
    return "home"

@app.route("/random", methods = ["GET"])
def randomTweet():
    """randomTweet"""
    doc = t.getRandomDocument("UBI", "tweets")
    response = flask.jsonify({"tweet" : str(doc["content"])})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/size", methods = ["GET"])
def size():
    """size"""
    collectionSize = t.getCollectionSize("UBI", "tweets")
    response = flask.jsonify({"size" : collectionSize})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response