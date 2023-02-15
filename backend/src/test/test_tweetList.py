'''Tests for tweetList.py'''
import os
import pytest
from src.lib.tweetList import TweetList

@pytest.fixture
def emptyTweetList():
    '''Initialize an empty TweetList object.'''
    return TweetList()

def test_TweepyBearerToken(emptyTweetList):
    '''Test that the Tweepy client was given the correct bearer token.'''
    assert emptyTweetList.getTweepyBearerToken() == os.environ.get("BEARER_TOKEN")

def test_getMongoClientStatus(emptyTweetList):
    '''Test that the Mongo client is working.'''
    assert emptyTweetList.getMongoClientStatus() == "Server available"

def test_numTweetsInEmptyList(emptyTweetList):
    '''Ensure that the empty TweetList is indeed empty.'''
    assert emptyTweetList.getNumTweets() == 0

def test_readFromJSON(emptyTweetList):
    '''Test that readFromJSON() is working as intended.'''
    emptyTweetList.readFromJSON("tweets.json")
    assert emptyTweetList.getNumTweets() > 0

def test_pushToDB(emptyTweetList):
    '''Test that pushToDB() is working as intended.'''
    emptyTweetList.readFromJSON("tweets.json")
    emptyTweetList.pushToDB("UBI", "tweets")
    assert emptyTweetList.getCollectionSize("UBI", "tweets") > 0