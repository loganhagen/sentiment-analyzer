"""Class that handles Language Processing for our backend"""
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#Expecting the use of NLTK, plotly, pandas, and scikit-learn

class LanguageProcessing:
    """Class that handles Language Processing for our backend"""
    def __init__(self):
        """Initializes the VADER sentiment analyzer"""
        self.sentiment_analysis = SentimentIntensityAnalyzer()

    def getSentiment(self, text):
        """Return sentiment analysis data as pandas dataframe"""
        return self.sentiment_analysis.polarity_scores(text)

    def sentimentToDataFrame(self, sentiment_scores: dict):
        """Return sentiment analysis data as pandas dataframe"""
        sent = ['Negative', 'Neutral', 'Positive', 'Compound']
        vals = sentiment_scores.values()

        df = pd.DataFrame(sent, columns=['Sentiment'])
        df['Sentiment Score'] = vals

        return df

    def getDatabaseSentiment(self, dbc):
        """Return sentiment analysis of entire database collection"""
        db = dbc.client["UBI"]

        twitter_col = db[dbc.TWITTER]
        reddit_col = db[dbc.REDDIT]

        twitter_str = ""
        reddit_str = ""

        #Build string with all tweets
        for document in twitter_col.find({}):
            twitter_str += (str(document["content"]) + " ") 

        #Build string with all reddit posts
        for document in reddit_col.find({}): 
            reddit_str += (str(document["content"]) + " ")

        #get sentiment for tweets
        twitter_sentiment = self.getSentiment(twitter_str)

        #get sentiment for reddit posts
        reddit_sentiment = self.getSentiment(reddit_str)

        return twitter_sentiment, reddit_sentiment
