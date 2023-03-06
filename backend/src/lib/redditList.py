import os
import requests
import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import mongomock



#add environment variables for reddit username, password, client_id and secret_token

mongo_uri = 'mongodb://' + os.environ.get('MONGO_USERNAME') + ':' + os.environ.get('MONGO_PASSWORD') + '@' + os.environ.get('MONGO_HOSTNAME') + ':27017'
test_db = os.environ.get('DB_TEST')



class RedditList:
	"""Class that handles Reddit API"""

	def __init__(self):
		"""Initialize"""
		self.headers = {'User-Agent': 'dataFetcher'}
		self.res = self.getOAuthToken()

		self.mongo_client = None

		# Return a mock database to the client variable is the DB_TEST env variable is raised.
		if test_db == '1':
			self.mongo_client = mongomock.MongoClient()
		else:
			self.mongo_client = MongoClient(mongo_uri)

	def getOAuthToken(self):
		"""Returns OAuth token from Reddit API"""
		auth = requests.auth.HTTPBasicAuth(os.environ.get("CLIENT_ID"), os.environ.get("SECRET_TOKEN"))
		data = {
			'grant_type': 'password',
			'username': os.environ.get("REDDIT_USERNAME"),
			'password': os.environ.get("REDDIT_PASSWORD")
		}
		res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth, data=data, headers=self.headers, timeout=5)
		return res

	def getMongoClientStatus(self):
		try:
			self.mongo_client.admin.command('ismaster')
		except ConnectionFailure:
			return "Server not available"
		return "Server available"

	def getSubredditPosts(self):
		#hot 
		self.getHotPosts()
		#new 
		#rising
		return None
	
	def getHotPosts(self):

		TOKEN = self.res.json()['access_token']
		self.headers = {**self.headers, **{'Authorization': f"bearer {TOKEN}"}}
		redRes = requests.get('https://oauth.reddit.com/r/basicincome/hot',headers=self.headers,timeout=5)
		for post in redRes.json()['data']['children']:
			print(post['data']['title'])

	def getComments(self):
		return None
	

if __name__ == "__main__":
	reddit = RedditList()
	reddit.getHotPosts()