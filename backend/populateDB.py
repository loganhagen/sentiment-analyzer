from src.db.connect import DBConnect

dbc = DBConnect()

dbc.writeFileToCollection("UBI", "tweets", "tweets.json")
dbc.writeFileToCollection("UBI", "reddit_posts", "reddit_posts.json")
