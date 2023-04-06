"""API route for handling anything that graph plotting using Plotly"""
import nltk
from flask_restx import Namespace, Resource
from src.lib.languageProcessing import LanguageProcessing
from src.lib.graphPlotter import GraphPlotter
from src.db.connect import DBConnect

nltk.download('vader_lexicon')
nltk.download('stopwords')

api = Namespace('plot', description='Graph Plotting Related Operations')
lp = LanguageProcessing()
gp = GraphPlotter()
dbc = DBConnect()

class TwitterSentiment(Resource):
    """
    Creates a plot of the sentiment of a given tweets
    """
    def get(self, post_id):
        doc = dbc.getDocumentById("UBI", dbc.TWITTER, post_id)
        text = dbc.cleanString(str(doc["content"]))
        sentiment = lp.getSentiment(text)
        df = lp.sentimentToDataFrame(sentiment)
        plot = gp.plotPostSentiment(df)

        return plot
    
class RedditSentiment(Resource):
    """
    Creates a plot of the sentiment of a given tweets
    """
    def get(self, post_id):
        doc = dbc.getDocumentById("UBI", dbc.REDDIT, post_id)
        text = dbc.cleanString(str(doc["content"]))
        sentiment = lp.getSentiment(text)
        df = lp.sentimentToDataFrame(sentiment)
        plot = gp.plotPostSentiment(df)

        return plot

class DataBaseSentiment(Resource):
    """
    Creates a twin pair bar graph of the sentiment of all posts in the database
    """
    def get(self):
        with open('db_sentiment.json', 'r', encoding='utf-8') as file:
            db_plot = file.read()
            file.close()
            return db_plot

api.add_resource(TwitterSentiment, "/sentiment/tweets/<string:post_id>")
api.add_resource(RedditSentiment, "/sentiment/reddit/<string:post_id>")
api.add_resource(DataBaseSentiment, "/sentiment/all")
