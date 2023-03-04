import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import requests
import json
import mongomock


#add environment variables for reddit username, password, client_id and secret_token

mongo_uri = 'mongodb://' + os.environ.get('MONGO_USERNAME') + ':' + os.environ.get('MONGO_PASSWORD') + '@' + os.environ.get('MONGO_HOSTNAME') + ':27017'
test_db = os.environ.get('DB_TEST')

data = {
	'grant_type': 'password',
	'username': os.environ.get("REDDIT_USERNAME"),
	'password': os.environ.get("REDDIT_PASSWORD")
}

class RedditList:
	"""Class that handles Reddit API"""

	def __init__(self):
		"""Initialize"""
		self.mongo_client = None

		# Return a mock database to the client variable is the DB_TEST env variable is raised.
		if test_db == '1':
			self.mongo_client = mongomock.MongoClient()
		else:
			self.mongo_client = MongoClient(mongo_uri)

	def getMongoClientStatus(self):
		try:
			self.mongo_client.admin.command('ismaster')
		except ConnectionFailure:
			return "Server not available"
		return "Server available"

	def getSubredditPosts(self):
		return None

	def getComments(self):
		return None
	



auth = requests.auth.HTTPBasicAuth(os.environ.get("CLIENT_ID"), os.environ.get("SECRET_TOKEN"))



headers = {'User-Agent': 'dataFetcher'}

print(data)

res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

#print(headers)

#print(requests.get('https://oauth.reddit.com/api/v1/me', headers=headers))

redRes = requests.get('https://oauth.reddit.com/r/basicincome/hot',headers=headers)

#print(redRes.json())

for post in redRes.json()['data']['children']:
	print(post['data']['title'])
	