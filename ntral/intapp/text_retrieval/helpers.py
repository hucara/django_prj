import json
from gensim.parsing.preprocessing import STOPWORDS

def tokenize(text):
    return [
            token
            for token in gensim.utils.simple_preprocess(text)
            if token not in STOPWORDS
            ]

def iter_news(file):
    for line in open(file):
        line = json.loads(line)
        line = line['headline'] + line['short_description']
        tokens = tokenize(line)
        yield line, tokens
