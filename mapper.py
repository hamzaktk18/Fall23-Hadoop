#!/usr/bin/env python

import sys

#our mapper function to replace the list and print out <key,value> as <word,1>
def mapper_count(text):
    for word in text:
        word = word.strip()
        word = word.replace('[', '').replace(']', '').replace("'", "")
        print('{}\t{}'.format(word, '1')) #print <key, value> to the reducer

#using sys.stdin read directly instead of running a loop to ensure preprocessor output is taken care of
words = sys.stdin.read().split(', ')
mapper_count(words) #calling our function and return <key, value>