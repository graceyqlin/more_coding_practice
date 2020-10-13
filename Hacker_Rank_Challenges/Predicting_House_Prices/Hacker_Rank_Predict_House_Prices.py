# Predict_House_Prices.py

# Hacker_Rank_Challenges
# In this challenge, we practice using multiple linear regression to predict housing prices. Check out the Resources tab for helpful videos!

# Task
# Charlie wants to buy a house. He does a detailed survey of the area where he wants to live, in which he quantifies, normalizes, and maps the desirable features of houses to values on a scale of  to  so the data can be assembled into a table. If Charlie noted  features, each row contains  space-separated values followed by the house price in dollars per square foot (making for a total of  columns). If Charlie makes observations about  houses, his observation table has  rows. This means that the table has a total of  entries.

# Unfortunately, he was only able to get the price per square foot for certain houses and thus needs your help estimating the prices of the rest! Given the feature and pricing data for a set of houses, help Charlie estimate the price per square foot of the houses for which he has compiled feature data but no pricing.

# Important Observation: The prices per square foot form an approximately linear function for the features quantified in Charlie's table. For the purposes of prediction, you need to figure out this linear function.

# Recommended Technique: Use a regression-based technique. At this point, you are not expected to account for bias and variance trade-offs.

# Input Format

# The first line contains  space-separated integers,  (the number of observed features) and  (the number of rows/houses for which Charlie has noted both the features and price per square foot).
# The  subsequent lines each contain  space-separated floating-point numbers describing a row in the table; the first  elements are the noted features for a house, and the very last element is its price per square foot.

# The next line (following the table) contains a single integer, , denoting the number of houses for for which Charlie noted features but does not know the price per square foot.
# The  subsequent lines each contain  space-separated floating-point numbers describing the features of a house for which pricing is not known.

# Sample Input

# 2 7
# 0.18 0.89 109.85
# 1.0 0.26 155.72
# 0.92 0.11 137.66
# 0.07 0.37 76.17
# 0.85 0.16 139.75
# 0.99 0.41 162.6
# 0.87 0.47 151.77
# 4
# 0.49 0.18
# 0.57 0.83
# 0.56 0.64
# 0.76 0.18
# Sample Output

# 105.22
# 142.68
# 132.94
# 129.71

import sklearn
from sklearn import linear_model
import numpy
import pandas as pd

from sklearn.linear_model import LinearRegression

# When reading from Hacker Rank:

# import fileinput 

# temp = []  
# for f in fileinput.input(): 
#     temp.append(f)

# df = pd.DataFrame(temp)

# When reading from local files:

df = pd.read_fwf('input00.txt', delim_whitespace = True, header = None)
df = df.rename(columns = {df.columns[0]:'text'})

variable_num = int(df['text'][0].split(" ")[0])
training_cnt = int(df['text'][0].split(" ")[1])

df_training = pd.DataFrame(df['text'][1:training_cnt].str.split(" ").tolist())
training_label = df_training[variable_num]
training_features = df_training.iloc[:, :-1]

input_features = pd.DataFrame(df[training_cnt+2:]['text'].str.split(" ").tolist())
input_features

model = LinearRegression()
model.fit(training_features, training_label)

for out in model.predict(input_features):
    print("%.2f" % out)
