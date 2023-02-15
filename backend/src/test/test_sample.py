"""PyTest example to see if PyTest works in GitLab CI Pipeline"""
import pytest
from src.lib.tweetList import TweetList

@pytest.fixture
def emptyTweetList():
    return TweetList("AAAAAAAAAAAAAAAAAAAAAFvZlQEAAAAAKJ2aLLYYPFSQyRsPgwSonDACeT0%3DwJjK63Eys0ixVHxTaYjTs9eBgOIOrDkOKytKcixt1m4WX3X4Yi")

def func(test_var):
    """function"""
    return test_var + 1

def test_answer():
    """Function test"""
    assert func(3) == 4
