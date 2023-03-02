import requests
import json


#add environment variables for reddit username, password, client_id and secret_token

with open('password.json', 'r') as f:
	passwordData = json.load(f)

print(passwordData)



auth = requests.auth.HTTPBasicAuth(passwordData['CLIENT_ID'], passwordData['SECRET_TOKEN'])

data = {
	'grant_type': 'password',
	'username': passwordData['USERNAME'],
	'password': passwordData['PASSWORD']
}

headers = {'User-Agent': 'dataFetcher'}

res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

#print(headers)

#print(requests.get('https://oauth.reddit.com/api/v1/me', headers=headers))

redRes = requests.get('https://oauth.reddit.com/r/basicincome/hot',headers=headers)

#print(redRes.json())

for post in redRes.json()['data']['children']:
	print(post['data']['title'])
	