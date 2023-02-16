'''Tests for tweetList.py'''
import os
import pytest
from src.lib.tweetList import TweetList

os.environ["TEST_DB"] = '1'

@pytest.fixture
def emptyTweetList():
    '''Initialize an empty TweetList object.'''
    return TweetList()

@pytest.fixture()
def tweetList():
    '''Fixture which returns a TweetList object after reading data from a JSON
    file into memory.'''
    t = TweetList()
    t.readFromJSON("tweets_test.json")

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

def test_readFromJSONBadFile(emptyTweetList):
    '''Test ReadFromJSON with a bad file.'''
    with pytest.raises(FileNotFoundError):
        emptyTweetList.readFromJSON("badfile.json")

def test_pushToDBFromJSON(tweetList):
    '''Test that pushToDB() is working as intended.'''
    tweetList.pushToDB("UBI", "tweets_test")
    assert tweetList.getCollectionSize("UBI", "tweets_test") > 0

def test_writeCollectionToJSON(tweetList):
    '''Tests that the function is correctly
    writing to a JSON file'''
    os.remove("tweets_test.json")
    tweetList.writeCollectionToJSON("UBI", "tweets_test", "tweets_test.json")
    tweetList.emptyList()
    tweetList.readFromJSON("tweets_test.json")
    assert tweetList.getNumTweets() > 0

def test_getBadCollection(emptyTweetList):
    '''Get the collection size of a collection which does not exist.'''
    assert emptyTweetList.getCollectionSize("test", "test") == 0

def test_getRandomDocument(tweetList):
    '''Test getRandomDocument() with valid input.'''
    assert tweetList.getRandomDocument("UBI", "tweets") is not None

def test_getRandomDocumentBad(tweetList):
    '''Test getRandomDocument() with invalid input.'''
    assert tweetList.getRandomDocument("test", "test") is None

# @pytest.mark.parametrize("database, collection, expected", [
#     ("UBI", "tweets", not None),
#     ("test", "test", None)
# ])
# def test_funct(tweetList, database, collection, expected):
#     assert tweetList.getRandomDocument(database, collection) == expected
