# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:57:23 2017

@author: 1399869
"""

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

def extract_features(word_list):
    return dict([(word, True) for word in word_list])


# Load positive and negative reviews
positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')

features_positive = [(extract_features(movie_reviews.words(fileids=[f])),
            'Positive') for f in positive_fileids]
features_negative = [(extract_features(movie_reviews.words(fileids=[f])),
            'Negative') for f in negative_fileids]

    # Split the data into train and test (80/20)
threshold_factor = 0.8
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))

features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:] + features_negative[threshold_negative:]
#print('\nNumber of training datapoints:', len(features_train))

#print('Number of test datapoints:', len(features_test))

    # Train a Naive Bayes classifier
classifier = NaiveBayesClassifier.train(features_train)

def analyzer(review):
    probdist = classifier.prob_classify(extract_features(review.split()))
    pred_sentiment = probdist.max()
    b = round(probdist.prob(pred_sentiment), 2)
    a=dict()
    a.update({'Predicted sentiment': pred_sentiment})
    a.update({'Probability':b})
    print(a)
