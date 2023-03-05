"""app.py"""
import nltk
from flask.cli import FlaskGroup
from src import create_app

# I could not get the cached installation of nltk to work, so I had to do it when the backend starts running. - Kyle
# This installs the VADER sentiment analysis module from NLTK
nltk.download('vader_lexicon')

app = create_app()

cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
