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