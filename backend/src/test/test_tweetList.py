'''Tests for tweetList.py'''
import os
import pytest
from src.lib.tweetList import TweetList

@pytest.fixture
def emptyTweetList():
    '''Initialize an empty TweetList object.'''
    return TweetList()

@pytest.fixture()
def JSONTweetList():
    t = TweetList()
    t.readFromJSON("tweets.json")
    t.pushToDB("UBI", "tweets")

    return t

def test_TweepyBearerToken(emptyTweetList):
    '''Test that the Tweepy client was given the correct bearer token.'''
    assert emptyTweetList.getTweepyBearerToken() == os.environ.get("BEARER_TOKEN")

def test_getMongoClientStatus(emptyTweetList):
    '''Test that the Mongo client is working.'''
    assert emptyTweetList.getMongoClientStatus() == "Server available"

def test_numTweetsInEmptyList(emptyTweetList):
    '''Ensure that the empty TweetList is indeed empty.'''
    assert emptyTweetList.getNumTweets() == 0

def test_readFromJSON(JSONTweetList):
    '''Test that readFromJSON() is working as intended.'''
    assert JSONTweetList.getNumTweets() > 0

def test_readFromJSONBadFile(emptyTweetList):
    '''Test ReadFromJSON with a bad file.'''
    with pytest.raises(FileNotFoundError):
        emptyTweetList.readFromJSON("badfile.json")

def test_pushToDBFromJSON(JSONTweetList):
    '''Test that pushToDB() is working as intended.'''
    assert JSONTweetList.getCollectionSize("UBI", "tweets") > 0

def test_getBadCollection(emptyTweetList):
    assert emptyTweetList.getCollectionSize("test", "test") == 0

def test_getRandomDocutment(JSONTweetList):
    assert JSONTweetList.getRandomDocument("UBI", "tweets") is not None
