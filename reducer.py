#!/usr/bin/env python
import sys

def print_word_count(word, count):
    print('{}\t{}'.format(word, count))

current_word = None #Initializing empty string
current_count = 0 #Initializing empty string

word_counts = []

#read the input
for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    
   #sum up the counts of the same word
    if current_word == word:
        current_count += count
    else:
        #if the word is done counted store the count and move to next
        if current_word:
            word_counts.append((current_word, current_count))
            
        #initialize the new word and count
        current_word = word
        current_count = count
        
#check the count last word
if current_word:
    word_counts.append((current_word, current_count))
    
    #sort words with counts in descending order 
sorted_word_counts = sorted(word_counts, key=lambda x: x[1], reverse=True)
#output the reducer
for word, count in sorted_word_counts:
    print_word_count(word, count)
