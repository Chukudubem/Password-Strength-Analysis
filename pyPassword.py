import re
import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

input_file = "insert input file here"

filepath = "formatted_passwords.csv"
encoding='cp850'

with open(input_file, "r", encoding=encoding) as infile, open(filepath, "w",  encoding=encoding) as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for line in reader:
        newline = [','.join(line[:-1])] + line[-1:]
        writer.writerow(newline)

df = pd.read_csv(filepath, encoding=encoding)

df.fillna(" ", inplace=True) #In the case where password is null, replace with blank space

'''
    Feature creation:
    1. password lengths
    2. number of special characters used 
    3. number of digits used
    4. number of capitalization used
'''

# creating new column for password length 
# passing values through str.len() 
df["password_length"]= df["password"].str.len() 
df['special_characters'] = df['password'].str.count(r'[^a-zA-Z0-9 ]')
df['no_of_digits'] = df['password'].str.count(r'[0-9]')
df['capitalized_alphabets'] = df['password'].str.count(r'[A-Z]')

### Split the data into train & test sets
X = df.drop('strength', axis=1)
y = df['strength']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

### Logistic Regression

lr = LogisticRegression(penalty = 'l2', class_weight='balanced')
lr.fit(X_train.drop("password", axis=1), y_train)
prediction = lr.predict(X_test.drop("password", axis=1))

print(classification_report(y_test, prediction))
print(accuracy_score(y_test, prediction))