"""Scripts for operating on the database."""
from profanity_filter import ProfanityFilter
from src.lib.tweetList import TweetList

def censorTweets(database, collection):
    t = TweetList()
    pf = ProfanityFilter()
    db = t.mongo_client[database]
    col = db[collection]

    for document in col.find({}):
        col.update_one(document, {"$set": {"content" : pf.censor(document["content"])}})
