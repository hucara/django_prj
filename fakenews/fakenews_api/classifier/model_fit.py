import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer, HashingVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from joblib import dump, load

#1: unreliable
#0: reliable
print("Load data.")
print(os.getcwd())
train=pd.read_csv('fakenews_api/ingestion/rawdata/train.csv')
train.info()

#data prep
train=train.fillna(' ')
train['total']=train['title']+' '+train['author']+train['text']
targets = train['label'].values
"""
pipeline = Pipeline([('tfidf', TfidfVectorizer(smooth_idf=False, sublinear_tf=False, ngram_range=(1,2))),
                     ('clf', LogisticRegression(C=1e5))])
"""

pipeline = Pipeline([('tfidf', HashingVectorizer(ngram_range=(1,2))),
                     ('clf', LogisticRegression(C=1e5))])

#split in samples
X_train, X_test, y_train, y_test = train_test_split(train['total'], targets, random_state=0)

print("Fit model.")
pipeline.fit(X_train, y_train)
print('Accuracy of Lasso classifier on training set: {:.2f}'
     .format(pipeline.score(X_train, y_train)))
print('Accuracy of Lasso classifier on test set: {:.2f}'
     .format(pipeline.score(X_test, y_test)))

print("Serialize model.")
dump(pipeline._final_estimator, 'fakenews_api/classifier/serialized_models/logreg.joblib', compress = 3)
dump(pipeline.named_steps['tfidf'], 'fakenews_api/classifier/serialized_models/count_vectorizer.joblib', compress = 3)
