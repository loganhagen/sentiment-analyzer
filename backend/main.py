import pandas as pd
from src.db.connect import DBConnect

dbc = DBConnect()
tweets_obj = dbc.getCollectionJSON("UBI", "tweets")
tweets = tweets_obj["data"]
id = []
for tweet in enumerate(tweets):
    id.append(tweet["_id"])

for i in enumerate(id):
    print(i)


df = pd.DataFrame()
df["id"] = ["1231312", "1123123", "2342423"]
df["polarity"] = [0.1, 1.5, -0.2]