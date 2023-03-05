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
