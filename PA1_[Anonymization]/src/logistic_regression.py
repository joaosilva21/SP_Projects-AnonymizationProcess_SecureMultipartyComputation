import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# read dataset
df = pd.read_csv('TREINO_MIX.csv', sep=';')

# drop non relevant columns
df.drop('name', axis=1, inplace=True)
df.drop('social_number', axis=1, inplace=True)

# drop suprassed lines
m = 1768
df = df.drop(df.index[-m:], axis=0)

interval_dummies_age = pd.get_dummies(df["age"])
interval_dummies_height = pd.get_dummies(df["height"])
interval_dummies_weight = pd.get_dummies(df["weight"])

df.drop('age', axis=1, inplace=True)
df.drop('height', axis=1, inplace=True)
df.drop('weight', axis=1, inplace=True)

X = pd.concat([df.iloc[:,:-1], interval_dummies_age], axis=1)
X = pd.concat([df.iloc[:,:-1], interval_dummies_height], axis=1)
X = pd.concat([df.iloc[:,:-1], interval_dummies_weight], axis=1)
y = df["cardio"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
classification = classification_report(y_test, y_pred)
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", confusion)
print("Classification Report:\n", classification)
