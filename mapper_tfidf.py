#!/media/finalproject/myenv

import sys
#This library is the reason we are activiting virtual env python
from sklearn.feature_extraction.text import TfidfVectorizer


#help from : https://kavita-ganesan.com/tfidftransformer-tfidfvectorizer-usage-differences/
def mapper_tfidf(text, doc_id):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([' '.join(text)])
    feature_names = vectorizer.get_feature_names_out()

    #print <key, value> to the reducer
    for i, word in enumerate(feature_names):
        print('{}\t{}\t{}'.format(word, doc_id, tfidf_matrix[0, i]))


words = sys.stdin.read().split(',')
mapper_tfidf(words, sys.argv[1]) #calling our function and return <key, value>