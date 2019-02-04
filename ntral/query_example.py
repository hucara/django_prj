import requests
import sys

def send():

    search = [{'query': 'illness', 'return': 10}]

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    r = requests.post(
        'http://127.0.0.1:8000/api/search/',
        json=search, headers=headers
    )
    sys.stdout.write(r.text)


if __name__ == "__main__":
    send()
