import pandas as pd
import nltk
from nltk.corpus import stopwords

# nltk.download('stopwords')      # uncomment this line for first run

def removeStopWords(tokenizeResult):
    stopWords = set(stopwords.words('english'))
    filteredSentence = [w for w in tokenizeResult if not w.lower() in stopWords]

    return filteredSentence

