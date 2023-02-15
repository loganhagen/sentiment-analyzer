"""PyTest example to see if PyTest works in GitLab CI Pipeline"""
import os
import pytest
from src.lib.tweetList import TweetList

@pytest.fixture
def emptyTweetList():
    return TweetList()

def test_TweepyBearerToken(emptyTweetList):
    assert emptyTweetList.getTweepyBearerToken() == os.environ.get("BEARER_TOKEN")