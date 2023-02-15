"""Script that pushes tweets to your local database from a the tweets.json file"""

from src.lib.tweetList import TweetList

t = TweetList()

t.readFromJSON("tweets.json")
t.writeToCSV("tweets.csv")

t.pushToDB("UBI", "tweets")
