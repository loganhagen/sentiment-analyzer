"""Class that uses Plotly to generate graph data to be passed to PlotlyJS as a JSON object."""
import plotly.express as px
import pandas as pd

class GraphPlotter:
    """Class that uses Plotly to generate the graphs that will be used in the app"""
    def plotPostSentiment(self, df: pd.DataFrame, title:str=None, x_label:str=None, y_label:str=None):
        """Generates a bar graph of the sentiment analysis data frame from a post"""
        fig = px.bar(
            data_frame=df, 
            orientation='h',
            color='Sentiment',
            title='Sentiment Analysis of Post',
            x='Sentiment Score',
            y='Sentiment',
            range_x=[0,1],
        )

        if x_label is not None:
            fig.update_layout(
                xaxis_title=x_label,
            )
        
        if y_label is not None:
            fig.update_layout(
                yaxis_title=y_label,
            )

        if title is not None:
            fig.update_layout(
                title=title,
            )

        result = fig.to_json()
        return result