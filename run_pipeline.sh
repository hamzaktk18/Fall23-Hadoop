#!/bin/bash
source myenv/bin/activate #activiting virtual env python which is separate than the majaro default python

echo "Output for fp_output.txt:" | tee -a ~/results/output_final.txt #help from: https://phoenixnap.com/kb/linux-tee
cat fp_output.txt | python preprocess_tfidf.py | python mapper_tfidf.py doc1 | python reducer_tfidf.py | tee -a ~/results/output_final.txt

echo "Output for fp_output22.txt:" | tee -a ~/results/output_final.txt
cat fp_output22.txt | python preprocess_tfidf.py | python mapper_tfidf.py doc2 | python reducer_tfidf.py | tee -a ~/results/output_final.txt

deactivate #deactiviting the python env since the file is already outputted