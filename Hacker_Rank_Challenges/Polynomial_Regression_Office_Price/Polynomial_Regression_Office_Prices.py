# Polynomial_Regression_Office_Prices.py


# https://www.hackerrank.com/challenges/predicting-office-space-price/problem
# For those new to the topic of Polynomial Regression, here's a wonderful video of Dr. Andrew Ng from Stanford, explaining the topic. It might be helpful to watch this video and any other resources of your choice before proceeding with the problem.


# The Problem

# Charlie wants to purchase office-space. He does a detailed survey of the offices and corporate complexes in the area, and tries to quantify a lot of factors, such as the distance of the offices from residential and other commercial areas, schools and workplaces; the reputation of the construction companies and builders involved in constructing the apartments; the distance of the offices from highways, freeways and important roads; the facilities around the office space and so on.

# Each of these factors are quantified, normalized and mapped to values on a scale of 0 to 1. Charlie then makes a table. Each row in the table corresponds to Charlie's observations for a particular house. If Charlie has observed and noted F features, the row contains F values separated by a single space, followed by the office-space price in dollars/square-foot. If Charlie makes observations for H houses, his observation table has (F+1) columns and H rows, and a total of (F+1) * H entries.

# Charlie does several such surveys and provides you with the tabulated data. At the end of these tables are some rows which have just F columns (the price per square foot is missing). Your task is to predict these prices. F can be any integer number between 1 and 5, both inclusive.

# There is one important observation which Charlie has made.

# The prices per square foot, are (approximately) a polynomial function of the features in the observation table. This polynomial always has an order less than 4
# Input Format

# The first line contains two space separated integers, F and N. Over here, F is the number of observed features. N is the number of rows for which features as well as price per square-foot have been noted.
# This is followed by a table having F+1 columns and N rows with each row in a new line and each column separated by a single space. The last column is the price per square foot.

# The table is immediately followed by integer T followed by T rows containing F columns.

# Constraints

# 1 <= F <= 5
# 5 <= N <= 100
# 1 <= T <= 100
# 0 <= Price Per Square Foot <= 10^6 0 <= Factor Values <= 1

# Output Format

# T lines. Each line 'i' contains the predicted price for the 'i'th test case.

# Sample Input

# 2 100
# 0.44 0.68 511.14
# 0.99 0.23 717.1
# 0.84 0.29 607.91
# 0.28 0.45 270.4
# 0.07 0.83 289.88
# 0.66 0.8 830.85
# 0.73 0.92 1038.09
# 0.57 0.43 455.19
# 0.43 0.89 640.17
# 0.27 0.95 511.06
# 4
# 0.05 0.54
# 0.91 0.91
# 0.31 0.76
# 0.51 0.31
# Sample Output

# 180.38
# 1312.07
# 440.13
# 343.72
# Explanation

# There are two features which have been noted by Charlie. There are 100 data points, for which he has taken note of the features, and the price per square foot (in the last column).

# At the end, are four rows where he knows the two features, you output the predicted price/square foot of the office space for every testcase.

# Recommended Technique

# Use a regression based technique. At this point, you are not expected to account for bias and variance trade-offs.


# Enter your code here. Read input from STDIN. Print output to STDOUT

import sklearn
from sklearn import linear_model
import numpy
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV, ShuffleSplit
from sklearn.metrics import classification_report, accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# import matplotlib.pyplot as plt
# import seaborn as sns

import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

import fileinput
temp = []  
for f in fileinput.input(): 
    temp.append(f)

df = pd.DataFrame(temp)
df[0] = df[0].str.replace('\n', '')

first_line = df[0][0]
feature_num = int(first_line.split(' ')[0])
train_cnt = int(first_line.split(' ')[1])
input_cnt = df[0][train_cnt+1]

df_train_validation = pd.DataFrame(df[1:train_cnt+1][0].str.split(" ").tolist())

df_train, df_validation = train_test_split(df_train_validation, test_size=.2)

X_train = df_train[df_train.columns[:-1]]
y_train = df_train[df_train.columns[-1]]

X_validation = df_validation[df_validation.columns[:-1]]
y_validation = df_validation[df_validation.columns[-1]]

model = RandomForestRegressor()
model.fit(X_train, y_train)
y_validation_pred = model.predict(X_validation)

df_input = pd.DataFrame(df[train_cnt+2:][0].str.split(" ").tolist())

for i in model.predict(df_input):
    print("%.2f" % i)
