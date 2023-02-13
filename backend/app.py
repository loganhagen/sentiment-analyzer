"""app.py"""

import os
import tweetList
from flask import Flask

app = Flask(__name__)

t = tweetList.TweetList(os.environ.get("BEARER_TOKEN"))

@app.route("/")
def hello_world():
    """hello_world"""
    return "home"

@app.route("/random", methods = ["GET"])
def tweet():
    """tweet"""
    doc = t.getRandomDocument("UBI", "tweets")

    return doc["content"]

@app.route("/size", methods = ["GET"])
def size():
    """size"""
    collectionSize = t.getCollectionSize("UBI", "tweets")

    return str(collectionSize)