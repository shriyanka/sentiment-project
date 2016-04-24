"""
Project: Sentiment Analysis using Background History data
Module 3: Preparing Feature set and training Classifier
Round 1: Feature set preparation
Round 2: Passing Feature set to NaiveBayesClassifier
Tools: Python, Nltk, Textblob 
References: 14.139.183.250:8080/bitstream/handle/123456789/120/Natural%20Language%20Processing%20with%20Python%20(2009).pdf?sequence=1
Date: 10th Feb, 2016
"""

from textblob.classifiers import NaiveBayesClassifier
import nltk
import random
from nltk.corpus import movie_reviews
import pickle


####################################################################
# Feature Functions
####################################################################

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

def testClassifier(cl):
    x = 1
    while x==1:
        sen = raw_input("Enter any statement")
        print cl.classify(sen)
        x = input("Continue - 1, Exit - 0")

######################################################################
# Script for perparing feature set and training and testing Classifier
######################################################################

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:2000]

featuresets = [(find_features(rev), category) for (rev, category) in documents]

#set that we'll train our classifier with
training_set = documents[0:100]#featuresets[:100] #documents[0:100] #

# set that we'll test against.b
testing_set = documents[101:200] # featuresets[101:200] #documents[101:200] #

try:
    classifier_f = open("naivebayesclassifier.pickle", "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
except:
    classifier = NaiveBayesClassifier(training_set)
    save_classifier = open("naivebayesclassifier.pickle","wb")
    pickle.dump(classifier, save_classifier)
    save_classifier.close()

cl = classifier

print "Classifier Ready to be used. Press Test - 1 Exit - 0"
x = input()
if x == 1:
    testClassifier(cl)
