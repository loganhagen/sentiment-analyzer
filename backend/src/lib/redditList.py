import os
from datetime import datetime
import requests



class RedditList:
    """Class that handles Reddit API"""

    def __init__(self):
        """Initialize"""
        self.headers = {'User-Agent': 'dataFetcher'}
        self.res = self.getOAuthToken()
        self.postList = []
        self.commentList = []
        self.query_result = None
        self.mongo_client = None



    def getOAuthToken(self):
        """Returns OAuth token from Reddit API"""
        auth = requests.auth.HTTPBasicAuth(os.environ.get("CLIENT_ID"), os.environ.get("SECRET_TOKEN"))
        data = {
            'grant_type': 'password',
            'username': os.environ.get("REDDIT_USERNAME"),
            'password': os.environ.get("REDDIT_PASSWORD")
        }
        #may have to write a function to refresh the token when it expires for asynchronous calls to reddit api when the program is hosted on kubernetes
        res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth, data=data, headers=self.headers, timeout=5)
        TOKEN = res.json()['access_token']
        self.headers = {**self.headers, **{'Authorization': f"bearer {TOKEN}"}}
        return res



    
    def getHotPosts(self):
        """Adds hot posts to postList"""
        redRes = requests.get('https://oauth.reddit.com/r/basicincome/hot',params={'limit': '100'},headers=self.headers,timeout=5)
        self.query_result = redRes.json()['data']['children']
        self.initPostList()


    def getNewPosts(self):
        """Adds new posts to postList"""	

        redRes = requests.get('https://oauth.reddit.com/r/basicincome/new',params={'limit': '100'},headers=self.headers,timeout=5)
        self.query_result = redRes.json()['data']['children']
        self.initPostList()



    def getTopPosts(self):
        """Adds top posts to list"""
        redRes = requests.get('https://oauth.reddit.com/r/basicincome/top',params={'limit': '100','t': 'all'},headers=self.headers,timeout=5)
        self.query_result = redRes.json()['data']['children']
        self.initPostList()


    def initPostList(self):
        """Adds posts to postList"""
        for child in self.query_result:
            title = child['data']['title']
            author = child['data']['author']
            created_utc = datetime.fromtimestamp(child['data']['created_utc'])
            post_id = child['data']['id']
            num_comments = child['data']['num_comments']

            #check if post exists in post list
            #i think this should be done in the database file as well
            #database should check by id for repeating posts
            if not self.postExists(post_id):
                post = self.Post(
                        title,
                        author,
                        post_id,
                        created_utc
                    )
                self.postList.append(post)
                post.setNumComments(num_comments)

    def getPostList(self):
        """Returns the post list"""
        return self.postList

    def postExists(self, post_id):
        """Returns true if post exists in postList"""
        for post in self.postList:
            if post.post_id == post_id:
                return True
        return False

    def getNumPosts(self):
        """Returns total number of posts"""
        return len(self.postList)

    def getComments(self):
        """Gets a list of comments for each post in postList"""
        if not self.postList:
            return False
        
        #FIX go through every post and add comments from the post
        url = 'https://oauth.reddit.com/r/basicincome/comments/' + str(self.postList[0].post_id)
        redRes = requests.get(url,params={'depth': '1'},headers=self.headers,timeout=5)
        self.query_result = redRes.json()[1]['data']['children']['data']
        self.initCommentList()


        return None
    
    def initCommentList(self):
        """Add Comments to the commentList"""
        for child in self.query_result:
            author = child['data']['author']
            body = child['data']['body']
            #convert to readable date time
            date = datetime.fromtimestamp(child['data']['created_utc'])
            #parse to get rid of t3
            post_id = child['data']['link_id']
            
            self.commentList.append(
                self.Comment(
                    author,
                    body,
                    post_id,
                    date
                )
            )

    
    class Post:
        """Class that represents a post"""
        def __init__(self, title, author, post_id, date):
            self.title = title
            self.author = author
            self.post_id = post_id
            self.date = date
            self.num_comments = 0
            self.commentList = []

        def getPostID(self):
            return self.post_id
        
        def setNumComments(self, num_comments):
            self.num_comments = num_comments
        
        def getTitle(self):
            return self.title
        
        def getDate(self):
            return self.date
        
        def toDict(self):
            """Returns dictionary representation of Post"""
            return {
                'title': str(self.title),
                'author': str(self.author),
                'post_id': str(self.post_id),
                'date': str(self.date)
            }
        
    class Comment:
        """Class that represents a a comment"""
        def __init__(self, author, body, post_id, date):
            self.author = author
            self.body = body
            self.post_id = self.parsePostID(post_id)
            self.date = date
      
        def getComment(self):
            """Returns comment"""
            return self.body
        
        def parsePostID(self, post_id):
            """Returns post id without subscript t3"""
            #FIX parse the post_id
            return post_id
        
        def toDict(self):
            """Returns dictionary representation of Comment"""
            #FIX
            return None

if __name__ == "__main__":
    reddit = RedditList()
    reddit.getTopPosts()
    reddit.getComments()