"""API route for handling anything that graph plotting using Plotly"""
import nltk
#from flask import Response, jsonify
from flask_restx import Namespace, Resource
from src.lib.tweetList import TweetList
from src.lib.languageProcessing import LanguageProcessing
from src.lib.graphPlotter import GraphPlotter

nltk.download('vader_lexicon')

api = Namespace('plot', description='Graph Plotting Related Operations')
t = TweetList()
lp = LanguageProcessing()
gp = GraphPlotter()

class SentimentPlot(Resource):
    """
    Creates a plot of the sentiment of a given tweets
    """
    
    def get(self, tweet_id):
        """Returns a plot of the sentiment of a given tweet"""

        doc = t.getDocumentById("UBI", "tweets", tweet_id)
        tweet_text = str(doc["content"])
        sentiment = lp.getSentiment(tweet_text)
        df = lp.sentimentToDataFrame(sentiment)

        plot = gp.plotTweetSentiment(df)

        return plot


api.add_resource(SentimentPlot, "/sentiment/<string:tweet_id>")