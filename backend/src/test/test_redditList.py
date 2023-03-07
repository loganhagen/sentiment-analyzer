'''Tests for redditList.py'''
import pytest
from src.lib.redditList import RedditList

@pytest.fixture()
def reddit():
    return RedditList()

def test_HotPosts(reddit):
    reddit.getHotPosts()
    post_list = reddit.getPostList()
    assert 100 == len(post_list)
