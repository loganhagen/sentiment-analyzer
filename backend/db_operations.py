"""Scripts for operating on the database."""
from profanity_filter import ProfanityFilter
from src.lib.tweetList import TweetList

t = TweetList()
pf = ProfanityFilter()

db = t.mongo_client["UBI"]
col = db["tweets"]

t.writeCollectionToJSON("UBI", "tweets", "tweets.json")

# for document in col.find({}):
#     str = document["content"]
#     str = pf.censor(str)

#     col.update_one(document, {"$set": {"content" : str}})

