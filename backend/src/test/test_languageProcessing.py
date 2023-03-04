"""Tests for languageProcessing.py"""
import unittest
import nltk
from src.lib.languageProcessing import LanguageProcessing

nltk.download('vader_lexicon')

def test_language_processing():
    """Initialize a languageProcessing object"""
    assert LanguageProcessing()

def test_get_sentiment():
    """Test the get_sentiment function against an example string with a known output"""
    test_str = "I really love NVIDIA"
    expected_results = [0.0, 0.308, 0.692, 0.6697]
    lp = LanguageProcessing()
    df = lp.get_sentiment(test_str)
    # Use unittest module to compare the results
    unittest.TestCase().assertListEqual(list(df['Sentiment Score']), expected_results)