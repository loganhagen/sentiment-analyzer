"""API route for handling anything that graph plotting using Plotly"""
import nltk
#from flask import Response, jsonify
from flask_restx import Namespace, Resource
from src.lib.languageProcessing import LanguageProcessing
from src.lib.graphPlotter import GraphPlotter
from src.db.connect import DBConnect

nltk.download('vader_lexicon')

api = Namespace('plot', description='Graph Plotting Related Operations')
lp = LanguageProcessing()
gp = GraphPlotter()
dbc = DBConnect()

class SentimentPlot(Resource):
    """
    Creates a plot of the sentiment of a given tweets
    """
    
    def get(self, collection, post_id):

        """Returns a plot of the sentiment of a given tweet"""
        if collection == "tweet":
            collection = "tweets"
        elif collection == "reddit":
            collection = "reddit"
        else:
            return {"message": "Invalid collection"}, 400

        doc = dbc.getDocumentById("UBI", collection, post_id)
        text = str(doc["content"])
        sentiment = lp.getSentiment(text)
        df = lp.sentimentToDataFrame(sentiment)

        plot = gp.plotPostSentiment(df)

        return plot


api.add_resource(SentimentPlot, "/sentiment/<string:collection>/<string:post_id>")