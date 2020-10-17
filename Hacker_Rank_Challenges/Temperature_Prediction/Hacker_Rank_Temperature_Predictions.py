# Hacker_Rank_Temperature_Predictions.py
# https://www.hackerrank.com/challenges/temperature-predictions/problem

# Objective
# In this challenge, we practice predicting values. Check out the Resources tab for some tips on approaching this problem.

# Task
# Given a record containing the maximum and minimum monthly temperatures at a particular station. The record shows the temperature information for each month in a data range from  to ; however, some of the temperature values have been blanked out! Estimate and print the missing values.


# Sample Input

# 20
# yyyy    month   tmax    tmin
# 1908    January 5.0 -1.4
# 1908    February    7.3 1.9
# 1908    March   6.2 0.3
# 1908    April   Missing_1   2.1
# 1908    May Missing_2   7.7
# 1908    June    17.7    8.7
# 1908    July    Missing_3   11.0
# 1908    August  17.5    9.7
# 1908    September   16.3    8.4
# 1908    October 14.6    8.0
# 1908    November    9.6 3.4
# 1908    December    5.8 Missing_4
# 1909    January 5.0 0.1
# 1909    February    5.5 -0.3
# 1909    March   5.6 -0.3
# 1909    April   12.2    3.3
# 1909    May 14.7    4.8
# 1909    June    15.0    7.5
# 1909    July    17.3    10.8
# 1909    August  18.8    10.7  

# Sample Output

# The four missing values are:

# 8.6
# 15.8
# 18.9
# 0.0    

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sklearn
from sklearn import linear_model
import numpy
import pandas as pd

from sklearn.linear_model import LinearRegression
import numpy as np
import fileinput

# Solution 1: Using Linear Regression:

# when read from local file:
# df = pd.read_csv('Temperature_Prediction_Sample.txt', header = 1, delim_whitespace=True)
# df = pd.get_dummies(df, columns=['month'])

# when read from hackerrank:
temp = []  
for f in fileinput.input(): 
    temp.append(f)

df = pd.DataFrame(temp)
df[0] = df[0].str.replace('\n', '')
df = df[0].str.split('\t').apply(pd.Series)
df = df[1:]
new_header = df.iloc[0] 
df = df[1:] 
df.columns = new_header

df = pd.get_dummies(df, columns=['month'])
df = df.reset_index()

def training(column_name):
    # both tmax and tmin has to have values
    df_training = df[~df["tmax"].str.contains('Missing', na=False)]
    df_training = df_training[~df_training["tmin"].str.contains('Missing', na=False)]
    
    training_label = df_training[column_name]
    training_features = df_training.drop([column_name], axis=1)
    
    model = LinearRegression()
    model.fit(training_features, training_label)
    
    return model

min_model = training("tmin")
max_model = training("tmax")

for i in range(len(df)):
    row_val = df.loc[i, :]
    if 'Missing' in row_val['tmin']:
        min_feature = pd.DataFrame(row_val.drop(['tmin'])).T
        print(min_model.predict(min_feature)[0])
    if 'Missing' in row_val['tmax']:
        max_feature = pd.DataFrame(row_val.drop(['tmax'])).T
        print(max_model.predict(max_feature)[0])


# Solution 2: Using Pandas Interpolation:
df2 = df.copy()

missing_index = []
for i in range(len(df)):
    for j in range(len(df.loc[0])):
        if 'Missing' in str(df.loc[i][j]):
            missing_index.append([i,j])

df2.loc[df2['tmax'].str.contains('Missing'), 'tmax'] = np.nan
df2.loc[df2['tmin'].str.contains('Missing'), 'tmin'] = np.nan

#Careful!! interpolate method only works on float64 data
cols = df2.columns

for col in cols:
    df2[col] = pd.to_numeric(df2[col], errors='coerce')
    
df2['tmax'] = df2['tmax'].interpolate()


df2['tmin'] = df2['tmin'].interpolate()

for r, c in missing_index:
    # print("%.2f" % df2.loc[r][c])
    print(round(df2.loc[r][c], 2))
