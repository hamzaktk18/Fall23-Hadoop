#!/media/finalproject/myenv/bin/python
import sys
import re
import spacy

nlp = spacy.load("en_core_web_sm") #Loading model for lemmatization help from - https://www.projectpro.io/recipes/install-and-use-spacy-models

stopwords = ['the', 'of', 'to', 'and', 'a', 'or', 'in', 'for', 'student', 'be', 'is', 'university', 'students', 'by', 'are',
    'with', 'will', 'on', 'not', 'that', 'an', 'may', 'as', 'any', 'at', 'eku', 'academic', 'from', 'if', 'policy',
    'this', 'conduct', 'all', 'community', 'information', 'office', 'their', 'other', 'have', 'who',
    'campus', 'services', 'which', 'must', 'you', 'should', 'andor', 'kentucky', 'can', 'has', 'exciting', 'exception', 'exceptional', 'exceptionality', 'exceptions', 'excessive', 'exchange', 'excite', 'exclude']

def remove_stopwords(text):
    return [word for word in text if word not in stopwords] #our defined function for removing stopwords

#function to clean up input text
def preprocessing(text):
    #replacing quotes, periods, commas and apostrophes
    #replacing / - uppercase, links and special characters plus URLs help from: https://gist.github.com/MrEliptik/b3f16179aa2f530781ef8ca9a16499af
    text = text.replace(' ,', '').replace(' -', '').replace('.', '').replace(',', '').replace('-', '').replace("'", '')
    mypattern = r'[^a-zA-Z\s,\'-]|(\d+)|(https?://\S+)'
    result_str = re.sub(mypattern, '', text)
    result_str = re.sub(r'\s+', ' ', result_str)
    result_str = result_str.lower()
    result_str = result_str.split()
    result_str = sorted(result_str)
    result_str = remove_stopwords(result_str)
    return result_str

#lemmatizing the strings to be done after preprocessing
def lemmatize(text):
    doc = nlp(" ".join(text)) #using the spacy model
    tokens = [token.text for token in doc]
    lemmatized_tokens = [token.lemma_ for token in doc] #list comprehension to find lemma (root word) help from - https://ashutoshtripathi.com/2020/04/06/guide-to-tokenization-lemmatization-stop-words-and-phrase-matching-using-spacy/
    return tokens, lemmatized_tokens

#actual mapping for the LDA
def map(text):
    for i in text:
        for j in i:
            print('{}\t{}'.format(j, '1'))

mytext = ""

for line in sys.stdin:
    mytext += line

preprocessed_text = preprocessing(mytext)
lemmatized_text = lemmatize(preprocessed_text)
map(lemmatized_text)