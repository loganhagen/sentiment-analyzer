from src.lib.twitter import Twitter
from src.db.connect import DBConnect

twitter = Twitter()
dbc = DBConnect()
QUERY = '("universal basic income") -is:retweet -is:reply -has:links -has:media lang:en'

twitter.getRecentTweets(QUERY, 1000)
twitter.writeToJSON("tweets.json")
dbc.writeFileToCollection(dbc.DB, dbc.TWITTER, "tweets.json")