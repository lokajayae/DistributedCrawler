import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def tokenizeReview(df):
    for r in df:
        cleaned = r['body'].strip('\n')
        r['words'] = word_tokenize(cleaned)