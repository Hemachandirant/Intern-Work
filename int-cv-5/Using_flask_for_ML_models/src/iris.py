import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('Dataset.csv')

df = df.drop(columns = ['Id'])

X = np.array(df.iloc[:, 0:4])
y = np.array(df.iloc[:, 4:])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y.reshape(-1))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LogisticRegression
sv = LogisticRegression().fit(X_train,y_train)

# print metric to get performance
print("Accuracy: ",sv.score(X_test, y_test) * 100)

pickle.dump(sv, open('iri.pkl', 'wb'))