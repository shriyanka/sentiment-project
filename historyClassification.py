"""
Project: Sentiment Analysis using Background History data
Module 4: Classification of history text
Tools: Python, Nltk, Textblob 
Date: 12th Feb, 2016
"""

import rawClassifier

print "Analyzing HIstory Texts"

fopen = '/home/kajal/sentiment-project/word_tokens.txt'
f = open(fopen,'r')
raw = (f.read()).split("\n")
pos,neg=0,0

for word in raw[:200]:
	x = rawClassifier.Classify(rawClassifier.cl, word)
	if x == 'pos':
		pos+=1
	else:
		neg+=1
	if (pos%50 or neg%50) == 0:
		print "Wait... Analyzing..."

#print pos,neg

print "Enter the Raw text to be analyzed"
text = raw_input()
sen = rawClassifier.Classify(rawClassifier.cl, text)

print "Result:\nFrom History - %s, From Text - %s"%(('pos' if pos>neg else 'neg'),sen)
