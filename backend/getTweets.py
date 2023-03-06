"""Script that retreives a specified number of Tweets using a specified query."""
from src.lib.tweetList import TweetList

t = TweetList()
QUERY = '"partial basic income" -is:retweet -has:links -has:media lang:en'

t.getRecentTweets(QUERY, 1000)
t.pushToDB("UBI", "tweets")
