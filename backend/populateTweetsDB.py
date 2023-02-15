"""Script that pushes tweets to your local database from a the tweets.json file"""

from src.lib.tweetList import TweetList

t = TweetList("AAAAAAAAAAAAAAAAAAAAAFvZlQEAAAAAKJ2aLLYYPFSQyRsPgwSonDACeT0%3DwJjK63Eys0ixVHxTaYjTs9eBgOIOrDkOKytKcixt1m4WX3X4Yi")

t.readFromJSON("tweets.json")

t.pushToDB("UBI", "tweets")