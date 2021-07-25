import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt')        # uncomment this for first run

def tokenizeReview(sentences):
    cleaned = sentences.strip('\n')     # remove new line
    words = word_tokenize(cleaned)

    return words