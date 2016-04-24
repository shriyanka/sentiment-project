import nltk
import random
from nltk.corpus import movie_reviews
import pickle

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

#print(documents[1])


all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(100))
#print(all_words["stupid"])
#print len(documents)

word_features = list(all_words.keys())[:2000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]
#print featuresets

#set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1950:1951]

try:
    classifier_f = open("naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
except:
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    save_classifier = open("naivebayes.pickle","wb")
    pickle.dump(classifier, save_classifier)
    save_classifier.close()

print("\n\nClassifier accuracy percent:",(nltk.classify.accuracy(classifier, training_set))*100)
#print dir(classifier)
#print classifier
#print classifier.show_most_informative_features(100)
