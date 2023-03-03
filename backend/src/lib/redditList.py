import os
from pymongo import MongoClient
import requests
import json


#add environment variables for reddit username, password, client_id and secret_token



auth = requests.auth.HTTPBasicAuth(os.environ.get("CLIENT_ID"), os.environ.get("SECRET_TOKEN"))

data = {
	'grant_type': 'password',
	'username': os.environ.get("REDDIT_USERNAME"),
	'password': os.environ.get("REDDIT_PASSWORD")
}

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
	