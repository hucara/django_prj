import requests
import datetime
import pandas as pd
import numpy as np
import json
import sys, os

#1: unreliable
#0: reliable
def ingest():
    print(os.getcwd())
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "rawdata")
    train=pd.read_csv(os.path.join(path, 'train.csv'))
    test=pd.read_csv(os.path.join(path, 'test.csv'))

    train = train.fillna(' ')
    test = test.fillna(' ')
    print("Ingestion train: {}".format(train.shape[0]))
    send(train, is_train = True)
    print("Ingestion test: {}".format(test.shape[0]))
    #send(test)

def send(data, is_train = False):
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    reports = []
    for idx, row in data.iterrows():
        data = {'title' : str(row['title']),
                'author' : str(row['author']),
                'content' : str(row['text']),
                'is_train' : is_train,
                'label' :  int(row['label'])}

        reports.append(data)

        if len(reports) > 100:
            r = requests.post('http://127.0.0.1:8000/api/reports/',
                              json = reports, headers = headers)
            sys.stdout.write("Batch inserted...")
            reports = []

            try:
                 r.raise_for_status()
            except requests.exceptions.RequestException as e:
                print("Error: " + str(e))
                print(r.headers)
                print(r.text)

if __name__ == "__main__":
    ingest()
