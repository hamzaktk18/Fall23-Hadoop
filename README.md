**Big Data - CSC 782
Fall 2023 - MS in CS at EKU
Final Project - Textual Analysis of the EKU Student Handbook 2022 using Word Count, Term Frequency - Inverse Document Frequency and Latent Dirichlet Allocation**

<ins> This project has three components:

- Word Count using MapReduce framework in Hadoop, in Manjaro Linux. This part of the code reads the txt file that was processed using pdf2txt.py and preprocessed for zipf's law analysis, remove common words (stopwords), map and reduce, this part of the project was the only part that successfully ran on hdfs.
- TF-IDF MapReduce framework code and related bash pipeline script to preprocess, map, reduce and combine the data.
- LDA is not an effective technique in the MapReduce framework for Hadoop, but it is possible.
