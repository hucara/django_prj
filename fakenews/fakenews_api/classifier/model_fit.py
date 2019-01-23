import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import joblib

from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# 1: unreliable
# 0: reliable
print("Load data.")
print(os.getcwd())
train = pd.read_csv('fakenews_api/ingestion/rawdata/train.csv')
train.info()

# data prep
train = train.fillna(' ')
train['total'] = train['title']+' '+train['author']+train['text']
targets = train['label'].values

pipeline = Pipeline([('hashv', HashingVectorizer(ngram_range=(1, 2))),
                     ('clf', LogisticRegression(C=1e5))])

# split in samples
X_train, X_test, y_train, y_test = train_test_split(
    train['total'], targets, random_state=0
)

print("Fit model.")
pipeline.fit(X_train, y_train)
print(
    'Accuracy of Lasso classifier on training set: {:.2f}'.format(
        pipeline.score(X_train, y_train))
)
print(
    'Accuracy of Lasso classifier on test set: {:.2f}'.format(
        pipeline.score(X_test, y_test))
)

print("Serialize model.")
joblib.dump(
    pipeline._final_estimator,
    'fakenews_api/classifier/serialized_models/logreg.joblib', compress=3
)

joblib.dump(
    pipeline.named_steps['hashv'],
    'fakenews_api/classifier/serialized_models/count_vectorizer.joblib',
    compress=3
)
