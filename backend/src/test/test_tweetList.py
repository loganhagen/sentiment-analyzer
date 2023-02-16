'''Tests for tweetList.py'''
import pytest
from src.lib.tweetList import TweetList

@pytest.fixture
def emptyTweetList():
    '''Initialize an empty TweetList object.'''
    return TweetList()
