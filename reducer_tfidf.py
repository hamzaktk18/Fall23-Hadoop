#!/media/finalproject/myenv
import sys

current_word = None
current_tfidf_sum = 0
document_count = 0

word_tfidfs = [] #list to save the values

for line in sys.stdin:
    try:
        parts = line.strip().split('\t') #Output was tricky to get so using tabs
        if len(parts) != 3: #Word, count, value
            raise ValueError("Invalid input format")
            
        word = parts[0]
        tfidf = float(parts[2])  # TF-IDF value for my word

        if current_word == word:
            current_tfidf_sum += tfidf
            document_count += 1
        else:
            if current_word:
                avg_tfidf = current_tfidf_sum / document_count
                word_tfidfs.append((current_word, avg_tfidf))
            current_word = word
            current_tfidf_sum = tfidf
            document_count = 1 #My number of documents, can be changed to 2
    except ValueError as e:
        print("Error processing line: {}".format(line.strip()))
        print("Error message: {}".format(str(e)))
        continue #Gave us alot of issues due to spacing and formatting

if current_word:
    avg_tfidf = current_tfidf_sum / document_count
    word_tfidfs.append((current_word, avg_tfidf))

sorted_word_tfidfs = sorted(word_tfidfs, key=lambda x: x[1], reverse=True)

sys.stdout.write("{:<20} {:<10}\n".format("Word", "Avg_TF-IDF"))
sys.stdout.write("-" * 30 + "\n") #using these for header and making it look pleasant
#sys.stdout.write instead of print because simple print is giving us issues
for word, avg_tfidf in sorted_word_tfidfs:
    sys.stdout.write("{:<20} {:.6f}\n".format(word, avg_tfidf))
