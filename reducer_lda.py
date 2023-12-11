#!/media/finalproject/myenv/bin/python
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

document = "" #ideally there would be more than 2 documents here, for project purposes we are only using one document and updating it in for-loop line(10)

for line in sys.stdin:
    word, count = line.strip().split('\t')
    document += f"{word} " * int(count)

vectorizer = CountVectorizer()
dtm = vectorizer.fit_transform([document])

lda = LatentDirichletAllocation(n_components=1, random_state=3) #selecting only one topic
lda.fit(dtm)

feature_names = vectorizer.get_feature_names_out() 

# help from - https://stackoverflow.com/questions/41275899/how-to-predict-the-topic-of-a-comment-in-the-following-lda-model
for topic_idx, topic in enumerate(lda.components_):
    top_words_idx = topic.argsort()[:-20-1:-1] #selecting only 20 terms for 1 topic sorted descending
    top_words = [feature_names[i] for i in top_words_idx] #printing out topics as a list
    print(f"Topic content: {', '.join(top_words)}")