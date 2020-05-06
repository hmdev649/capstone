import pandas as pd
import string, re

import nltk
from sklearn.feature_extraction import text

def tokenize(q):
    ''' tokenize and return a string of text '''
    pattern = "([a-zA-Z]+(?:'[a-z]+)?)"
    q_tokenized = nltk.regexp_tokenize(q, pattern)
    
    return q_tokenized

def lowercase(q):
    ''' convert all strings in a list to lowercase '''
    q_lower = [i.lower() for i in q]
    
    return q_lower

def rem_stop(q):
    ''' remove stop words from a list, return the new list '''
    stop_words = set(nltk.corpus.stopwords.words('english')).union({'watch'})
    q_stopped = [w for w in q if not w in stop_words]
    
    return q_stopped

def stem(q):
    ''' stem the words in a list, return the new list '''
    stemmer = nltk.SnowballStemmer("english")
    q_stem = [stemmer.stem(word) for word in q]
    
    return q_stem

