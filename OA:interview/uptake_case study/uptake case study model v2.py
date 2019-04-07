import pandas as pd
import numpy as np
from sklearn.model_selection import ShuffleSplit
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv('data/train.csv')

df[df == ' '] = np.nan
df['amount'] = df['amount'].fillna(0)

df['amount'][df['amount'] > 0] = 1

df = df.dropna(axis=1, thresh=df.shape[0]//2 + 1)
for col in df.columns:
    df[col] = df[col].fillna(df[col].value_counts().keys()[0])
    if df[col].dtype == 'object':
        df[col] = pd.factorize(df[col])[0]

df.drop(columns=['responded'], inplace = True)
train_label = df['amount']
df2 = pd.DataFrame()
for attri in df.columns:
    if attri != 'amount':
        df2[attri] = df[attri]
train_data = df2
print train_label.shape
print train_data.shape



clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(np.array(train_data), np.array(train_label))

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
scores = cross_val_score(clf, train_data, train_label, cv = cv)
print scores


test = pd.read_csv('data/test.csv')

temp = list(test.columns)
for col in temp:
    if col not in df.columns:
        #print(col)
        test = test.drop(columns=[col])

for col in test.columns:
    test[col] = test[col].fillna(df[col].value_counts().keys()[0])
    if test[col].dtype == 'object':
        test[col] = pd.factorize(test[col])[0]


predict = clf.predict(test)
print predict