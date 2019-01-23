import requests
import sys


def send():

    reports = []
    reports.append({
        'title': 'post title', 'author': 'post author',
        'content': 'post content', 'is_train': True, 'label': 0
        })

    reports.append({
        'title': 'post title', 'author': 'post author',
        'content': 'post content', 'is_train': True, 'label': 0
        })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    r = requests.post(
        'http://127.0.0.1:8000/api/reports/',
        json=reports, headers=headers
    )
    sys.stdout.write(r.text)


if __name__ == "__main__":
    send()
