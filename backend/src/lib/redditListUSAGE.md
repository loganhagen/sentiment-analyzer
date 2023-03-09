Using redditList API
    -   RedditList() to initialize the object
        - getHotPosts() gets 100 hot posts from /r/basicincome 
        - getTopPosts() gets 100 all time top posts from /r/basicincome
        - getNewPosts() gets 100 new posts from /r/basicincome

    - getComments() gets comments for all posts after calling the functions above
    - addCommentsToPost() add comments to its respective post
    - writeToJSON() returns a JSON representation of the redditList object
    - writeToFile(filename) writes the JSON object to a file 