from src.db.connect import DBConnect

dbc = DBConnect()
dbc.writeFileToCollection("UBI", "tweets", "tweets.json")