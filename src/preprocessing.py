import tokenization
import stopwords

def preprocessText(df):
    result = []
    for index, row in df.iterrows():
        tokenizeResult = tokenization.tokenizeReview(row['body'])
        filteredResult = stopwords.removeStopWords(tokenizeResult)

        preprocessResult = {
            'product': row['product'],
            'title': row['title'],
            'rating': row['rating'],
            'words': filteredResult
        }

        result.append(preprocessResult)

    return result
