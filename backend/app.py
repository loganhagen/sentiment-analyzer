"""app.py"""
from flask.cli import FlaskGroup
from src import create_app
# import nltk

app = create_app()
# nltk.download('vader_lexicon')

cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
