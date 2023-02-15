'''Tests for tweetList.py'''
import os
import pytest
from src.lib.tweetList import TweetList

@pytest.fixture
def emptyTweetList():
    '''Initialize an empty TweetList object.'''
    return TweetList()

@pytest.fixture()
def tweetList():
    '''Fixture which returns a TweetList object after reading data from a JSON
    file into memory as well as pushing it to the DB'''
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

def test_readFromJSON(tweetList):
    '''Test that readFromJSON() is working as intended.'''
    assert tweetList.getNumTweets() > 0

def test_pushToDBFromJSON(tweetList):
    '''Test that pushToDB() is working as intended.'''
    assert tweetList.getCollectionSize("UBI", "tweets") > 0

def test_writeCollectionToJSON(tweetList):
    '''Tests that the function is correctly
    writing to a JSON file'''
    tweetList.writeCollectionToJSON("UBI", "tweets", "tweets_test.json")
    tweetList.emptyList()
    tweetList.readFromJSON("tweets_test.json")
    assert tweetList.getNumTweets() > 0

def test_readFromJSONBadFile(emptyTweetList):
    '''Test ReadFromJSON with a bad file.'''
    with pytest.raises(FileNotFoundError):
        emptyTweetList.readFromJSON("badfile.json")

def test_getBadCollection(emptyTweetList):
    '''Get the collection size of a collection which does not exist.'''
    assert emptyTweetList.getCollectionSize("test", "test") == 0

def test_getRandomDocument(tweetList):
    '''Test getRandomDocument() with valid input.'''
    assert tweetList.getRandomDocument("UBI", "tweets") is not None

def test_getRandomDocumentBad(tweetList):
    '''Test getRandomDocument() with invalid input.'''
    assert tweetList.getRandomDocument("test", "test") is None
