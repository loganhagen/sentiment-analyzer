from src.lib.reddit import Reddit
from src.db.connect import DBConnect

#initialize
r = Reddit()
dbc = DBConnect()

#fetch new data
r.getNewPosts()
r.getComments()
r.addCommentsToPost()

#get jsonObject of new data
jsonObj = r.writeToJSON()

#add to database collection
dbc.writeJSONToCollection("UBI","reddit_posts",jsonObj)
