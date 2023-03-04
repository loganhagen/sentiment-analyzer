"""Class that handles Language Processing for our backend"""
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#Expecting the use of NLTK, plotly, pandas, and scikit-learn

class LanguageProcessing:
    """Class that handles Language Processing for our backend"""
    def __init__(self):
        """Initializes the VADER sentiment analyzer"""
        self.sentiment_analysis = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        """Return sentiment analysis data as pandas dataframe"""
        scores = self.sentiment_analysis.polarity_scores(text)

        sent = ['Negative', 'Neutral', 'Positive', 'Compound']
        vals = scores.values()

        df = pd.DataFrame(sent, columns=['Sentiment'])
        df['Sentiment Score'] = vals

        return df
