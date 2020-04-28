import pandas as pd
import string, re

import nltk
from sklearn.feature_extraction import text

def tokenize(q):
    pattern = "([a-zA-Z]+(?:'[a-z]+)?)"
    q_tokenized = nltk.regexp_tokenize(q, pattern)
    
    return q_tokenized

def lowercase(q):
    q_lower = [i.lower() for i in q]
    
    return q_lower

def rem_stop(q):
    stop_words = set(nltk.corpus.stopwords.words('english')).union({'watch'})
    q_stopped = [w for w in q if not w in stop_words]
    
    return q_stopped

def stem(q):
    stemmer = nltk.SnowballStemmer("english")
    q_stem = [stemmer.stem(word) for word in q]
    
    return q_stem

