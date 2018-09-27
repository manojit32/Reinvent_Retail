# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import textblob
from textblob import TextBlob as tb
from textblob.sentiments import NaiveBayesAnalyzer as nba
review=input("Please give your review about the shopping: ")
blob=tb(review, analyzer=nba())
print(blob.sentiment)