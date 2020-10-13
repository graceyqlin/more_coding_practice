#Hacker Rank Challenge:
#Document Category
# https://www.hackerrank.com/challenges/document-classification/problem
# You have been given a stack of documents that have already been processed and some that have not. 
# Your task is to classify these documents into one of eight categories: [1,2,3,...8]. 
# You look at the specifications on what a document must contain and are baffled by the jargon. 
# However, you notice that you already have a large amount of documents which have already been correctly 
# categorize (training data). You decide to use Machine Learning on this data in order to categorize the 
# uncategorized documents.

# Training Data

# In order to figure out what category each document should fall under you will base it on the categories of the documents in the "trainingdata.txt" file. This file will be included with your program at runtime and will be named "trainingdata.txt".

# The file is formatted as follows:

# The first line contains the number of lines that will follow.

# Each following line will contain a number (1-8), which is the category number. The number will be followed by a space then some space seperated words which is the processed document.

# Input

# The first line in the input file will contain T the number of documents. T lines will follow each containing a series of space seperated words which represents the processed document.

# Output

# For each document output a number between 1-8 which you believe this document should be categorized as.

# Sample Input

# 3
# This is a document
# this is another document
# documents are seperated by newlines

# Sample Output

# 1
# 4
# 8


import sys
from sklearn.feature_extraction import text
from sklearn import pipeline
from sklearn import linear_model
import numpy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit

def load_training_data(filename):
    df = pd.read_fwf(filename, delim_whitespace = True, header = None)
    df = df.rename(columns = {df.columns[0]:'text'})
    df = df[['text']][1:]
    df = pd.DataFrame(df['text'].str.split(" ", 1).tolist(), columns = ['category','text'])
    train_set, validation_set = train_test_split(df, test_size=.2)
    y_train = train_set['category']
    x_train = train_set['text']
    y_validation = validation_set['category']
    x_validation = validation_set['text']
    return x_train, y_train, x_validation, y_validation

def load_new_input_data(filename):
    df = pd.read_fwf(filename, delim_whitespace = True, header = None)
    df = df.rename(columns = {df.columns[0]:'text'})
    df = df[['text']][1:]
    x = df['text']
    return x

def vectorize_training_data(x):
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 1),
                              strip_accents='ascii', lowercase=True)
        x_vectorized = vectorizer.fit_transform(x)
        return x_vectorized, vectorizer   

def vectorize_testing_data(x_test, vectorizer):
    x_test_vectorized = vectorizer.transform(x_test)
    return x_test_vectorized

def train_model(model,x_vectorized, y):
        classifier = linear_model.SGDClassifier(class_weight='balanced')
        targets = y
        classifier.fit(x_vectorized, y)
        return classifier

def evaluate(model, x_validation_vectorized, y_validation):
        predictions = model.predict(x_validation_vectorized)
        print (classification_report(y_validation, predictions))
        print ("The accuracy score is {:.2%}".format(accuracy_score(y_validation, predictions)))


def find_best_parameter(input_model, param_grid, x_train_vectorized, y_train):
    cv_sets = ShuffleSplit(n_splits = 2, test_size = .33, random_state = 1)
    grid_search = GridSearchCV(estimator=input_model, param_grid=param_grid, cv = cv_sets, scoring='accuracy')
    grid_search.fit(x_train_vectorized, y_train)
    best_model = grid_search.best_estimator_
    return best_model

x_train, y_train, x_validation, y_validation = load_training_data('trainingdata.txt')

x_train_vectorized, vectorizer = vectorize_training_data(x_train)

x_validation_vectorized = vectorize_testing_data(x_validation, vectorizer)

model1 = LogisticRegression()
model = train_model(model1,x_train_vectorized, y_train)

# if we are running locally:
x_test = load_new_input_data('stdin.txt')


# when we are running in hacker rank:
import fileinput 
def load_hacker_rank_input():
	temp = []  
	for f in fileinput.input(): 
	    temp.append(f)
	df = pd.DataFrame(temp)
	df = df.rename(columns = {df.columns[0]:'text'})
	df['text'] = df['text'].str.replace('\n', '')
    df = df[['text']][1:]
    x = df['text']
    return x

x_test = load_hacker_rank_input()

x_test_vectorized = vectorize_testing_data(x_test, vectorizer)

for line in model.predict(x_test_vectorized):
    print(line)