"""
Project: Sentiment Analysis using Background History data
Module 2: Reading the Source content of each urls and preprocessing it
Round 1: 1st Round of preprocessing- Word Tokenization
Round 2: Initial preprocessing using nltk stopwords and explicit words
Tools: Python, Nltk-for preprocessing 
References: http://www.nltk.org/book/ch03.html
Date: 1st Feb, 2016
"""

import nltk, re, pprint
from nltk import word_tokenize
import subprocess
import time
import sys, os
from nltk.corpus import stopwords

WORD = []

EXLUDES_SYMBOLS = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-',\
	'+','=','{','}','[',']',':',';','"','\'','<',',','.','>','/','?','|','\\'\
	"''",'""']

EXLUDES_WORDS = ['a','and','the','or','if','i','can','we','am','should','in',\
	'at','on','how','where','why','as','me','us','into','you','to','be','by','do'\
	'I','will','shall','would','can','could','is','1','2','3','4','5','6'\
	'7','8','9','10','of','has','been','what','your']

EXLUDES_STOPWORDS = stopwords.words('english')

def file_tokenize(files):
	fopen = '/home/kajal/sentiment-project/rawdata/%s'%files
	print "************************************"+fopen+"*******************************"
	f = open(fopen,'r')
	raw = f.read()
	tokens = word_tokenize(raw.decode('utf-8'))
	WORD.append(tokens)

def read_files(path='/home/kajal/sentiment-project/rawdata/', sz=None):
    for dirname, dirnames, filenames in os.walk(path):
    	for files in filenames:
    		#ignoring the history files
    		if files == 'history.txt':
    			continue
        	f = file_tokenize(files)
                
r=read_files()
#print WORD

#writing the word in file instead of DB
f = open('/home/kajal/sentiment-project/word_tokens.txt','w')
for word in WORD:
	word = [x for x in word if x not in EXLUDES_SYMBOLS and x not in EXLUDES_WORDS and x not in EXLUDES_STOPWORDS]
	for w in word:
		f.write(w.encode("utf-8")+"\n")
