#!/media/finalproject/myenv

import sys
import re #to deal with regular expressions

#our stopwords based on most frequent words and our analysis of initial output using mapper and reducer
stopwords = ['the', 'of', 'to', 'and', 'a', 'or', 'in', 'for', 'student', 'be', 'is', 'university', 'students', 'by', 'are',
    'with', 'will', 'on', 'not', 'that', 'an', 'may', 'as', 'any', 'at', 'eku', 'academic', 'from', 'if', 'policy',
    'this', 'conduct', 'all', 'community', 'information', 'office', 'their', 'other', 'have', 'who',
    'campus', 'services', 'which', 'must', 'you', 'should', 'andor', 'kentucky', 'can', 'has']

#removing stopwords as the last step of preprocessing
def remove_stopwords(text):
    return [word for word in text if word not in stopwords]

#function to clean up input text
def preprocessing(text):
    text = text.replace(' ,', '').replace(' -', '').replace('.', '').replace(',', '').replace('-', '').replace("'", '') #replacing quotes, periods, commas and apostrophes
    #replacing / - uppercase, links and special characters plus URLs help from: https://gist.github.com/MrEliptik/b3f16179aa2f530781ef8ca9a16499af
    mypattern = r'[^a-zA-Z\s,\'-]|(\d+)|(https?://\S+)'
    result_str = re.sub(mypattern, '', text)
    result_str = re.sub(r'\s+', ' ', result_str)
    result_str = result_str.lower()
    result_str = result_str.split()
    result_str = sorted(result_str)
    result_str = remove_stopwords(result_str)
    return result_str

mytext = "" #empty string to hold my output
try:
    for line in sys.stdin:
        mytext += line

    words = preprocessing(mytext)
    print(','.join(words))

#Stackoverflow - error when mapper is still running but reducer wants output
except BrokenPipeError: # help from - https://stackoverflow.com/questions/14207708/ioerror-errno-32-broken-pipe-when-piping-prog-py-othercmd
    sys.stderr.close()
    sys.exit(0) 