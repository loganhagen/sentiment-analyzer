"""Initializes our API blueprint for our Flask app"""
from flask import Blueprint
from flask_restx import Api
from src.api.health import api as health_ns
from src.api.posts import api as posts_ns
from src.api.plot import api as plot_ns
from src.api.ask import api as ask_ns
from src.db.connect import DBConnect
from src.lib.graphPlotter import GraphPlotter
from src.lib.languageProcessing import LanguageProcessing

def saveDatabaseSentiment():
    lp = LanguageProcessing()
    gp = GraphPlotter()
    dbc = DBConnect()

    twitter_sentiment, reddit_sentiment = lp.getDatabaseSentiment(dbc)

    twitter_df = lp.sentimentToDataFrame(twitter_sentiment)
    reddit_df = lp.sentimentToDataFrame(reddit_sentiment)

    db_plot = gp.plotDatabaseSentiment(twitter_df, reddit_df)

    with open("db_sentiment.json", "w", encoding='utf-8') as file:
        file.write(db_plot)
        file.close()


# Create an API blueprint
api_bp = Blueprint("api", __name__)

# Create an API object with a title and description
api = Api(api_bp, title="Flask REST API", description="A RESTapi built with Flask")

# Add api namespaces to the api object that was created
api.add_namespace(health_ns)
api.add_namespace(posts_ns)
api.add_namespace(plot_ns)
api.add_namespace(ask_ns)

saveDatabaseSentiment()