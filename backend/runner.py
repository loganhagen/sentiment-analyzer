# import tweetList 
# import os

# if __name__ == "__main__":
#     query = '("universal basic income") -is:retweet lang:en'
#     bearer_token = "AAAAAAAAAAAAAAAAAAAAAFvZlQEAAAAAKJ2aLLYYPFSQyRsPgwSonDACeT0%3DwJjK63Eys0ixVHxTaYjTs9eBgOIOrDkOKytKcixt1m4WX3X4Yi"

    # t = tweetList.TweetList(os.environ.get("BEARER_TOKEN"))

    # Initialize the TweetList object. Initializes the Tweepy and Mongo clients as well.
    # t = tweetList.TweetList(bearer_token)

    # Search Twitter for up to 1000 Tweets from the last 2 weeks which match the given query.
    # t.getRecentTweets(query, 1000)

    # Read in Tweets from a local JSON file.
    # t.readFromJSON("tweets.json")

    # Write Tweets in memory to a local JSON file.
    # t.writeToJSON("tweets.json")

    # Push Tweets into the database.
    # t.pushToDB("UBI", "tweets")

    # Dump the specified collection into a local JSON file.
    # t.getDBdump("UBI", "tweets", "tweets.json")

    # Print the size of the specified collection.
    # print(t.getCollectionSize("UBI", "tweets"))

    # Print Tweets currently loaded into memory.
    # t.printTweetList()

    # Get the number of Tweets loaded in memory.
    # print(t.getNumTweets())

    # Print a random Tweet.
    # print(t.getRandomDocument("UBI", "tweets"))