import requests
import sys
import pandas as pd
import os


def send():
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fakenews_api", "ingestion", "rawdata"
        )
    train = pd.read_csv(os.path.join(path, 'train.csv'))
    reports = {}
    reports['title'] = train.head(1)['title']
    reports['author'] = train.head(1)['author']
    reports['content'] = train.head(1)['text']
    print(reports)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    r = requests.post('http://127.0.0.1:8000/api/clf/', data=reports)
    sys.stdout.write(r.text)


if __name__ == "__main__":
    send()
