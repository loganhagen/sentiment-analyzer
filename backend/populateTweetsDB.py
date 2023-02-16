"""Script that pushes tweets to your local database from a the tweets.json file"""

from src.lib.tweetList import TweetList

t = TweetList()

print(t.mongo_client.list_database_names())

# t.readFromJSON("tweets.json")

# t.pushToDB("UBI", "tweets")
