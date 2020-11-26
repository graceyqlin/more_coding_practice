# HackerRank_Calculate_TFIDF_Similarity_Scores

# https://www.hackerrank.com/challenges/nlp-similarity-scores/problem
# Combine:
import collections
import math
from math import log
import numpy as np


s= ["I'd like an apple", "An apple a day keeps the doctor away", "Never compare an apple to an orange", 
"I prefer scikit-learn to orange"]

processed = [document.lower() for document in s]

corpus = []
for document in processed:
    for word in document.split(" "):
        corpus.append(word)
corpus = set(corpus)


# calculate tf
def get_tf(document):
    tf = {}
    for (key, freq) in collections.Counter(document.split(" ")).items():
        tf[key] =  freq/len(document)
    return tf

# calculate idf
def get_idf(document):
    idf = {}
    for word in document.split(" "):
        document_has_word = 0
        for i in range(len(processed)):
            if word in processed[i]:
                document_has_word += 1
        # use smooth inverse document frequency:
        idf[word]  = log(len(processed) / ((document_has_word) + 1))
    return idf

# calculate tf_idf
def get_tf_idf(document):
    tf = get_tf(document)
    idf = get_idf(document)
    tf_idf = []
    for word in corpus:
        current_tf_idf = tf.get(word,0) * idf.get(word,0)
        tf_idf.append(current_tf_idf)
    return tf_idf


def get_cosine_similarity(document1, document2):
    v1 = get_tf_idf(document1)
    v2 = get_tf_idf(document2)
    numerator = np.dot(v1, v2)
    v1norm = (sum(v**2 for v in v1))**0.5
    v2norm = (sum(v**2 for v in v2))**0.5
    cosine_similarity = numerator/(v1norm * v2norm)
    return cosine_similarity


index_score_list = []
for i in range(1, len(processed)):
    score = get_cosine_similarity(processed[0], processed[i])
    index = i+1
    index_score_list.append((index, score))

top_index = sorted(index_score_list, key = lambda x: -x[1])[0][0]

print(top_index)