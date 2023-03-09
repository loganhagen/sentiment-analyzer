'''Tests for tweetList.py'''
import os
import pytest
from src.lib.twitter import Twitter

@pytest.fixture
def emptyTweetList():
    '''Initialize an empty TweetList object.'''
    return Twitter()

@pytest.fixture
def tweetList():
    '''Returns a TweetList object.'''
    t = Twitter()
    t.readFromJSON("tweets.json")
    return t

def test_tweepyBearerToken(emptyTweetList):
    '''Test that the Tweepy client was given the correct bearer token.'''
    assert emptyTweetList.getTweepyBearerToken() == os.environ.get("BEARER_TOKEN")

# def test_readFromJSON(emptyTweetList):
#     '''Loads 2282 tweets into the db from a local JSON file.'''
#     emptyTweetList.readFromJSON("tweets.json")
#     assert emptyTweetList.getNumTweets() == 2282

# def test_getDocumentById(emptyTweetList):
#     emptyTweetList.readFromJSON("tweets_test_input.json")
#     expected = "@MarioNawfal @AndrewYang #ChatGPT founder says AI will require a Universal Basic Income \n\nSam Altman says it should be paid out via cryptocurrency &amp; funded in part by the increased GDP created by AI https://t.co/ULUYQB3d2V"

#     doc = emptyTweetList.getDocumentById("UBI", "tweets", "1623133583446806529")
#     result = str(doc['content'])
#     assert result == expected