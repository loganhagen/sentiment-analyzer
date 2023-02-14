import src.lib.tweetList as tweetList
import os

if __name__ == "__main__":
    query = '("universal basic income") -is:retweet lang:en'
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAFvZlQEAAAAAKJ2aLLYYPFSQyRsPgwSonDACeT0%3DwJjK63Eys0ixVHxTaYjTs9eBgOIOrDkOKytKcixt1m4WX3X4Yi"

    t = tweetList.TweetList(os.environ.get("BEARER_TOKEN"))
    t.readFromJSON("tweets.json")
    print(t.getNumTweets())
