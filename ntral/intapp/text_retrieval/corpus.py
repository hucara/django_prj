from gensim.corpora import Dictionary
from helpers import iter_news
import gensim


class CorpusBuilder():

    def __init__(self, path):
        self.path = path
        self.dictionary = Dictionary()

    def __iter__(self):
        self.titles = []
        for title, tokens in iter_news(self.file):
            self.titles.append(title)
            yield self.dictionary.doc2bow(tokens)

    def build_dictionary(self, save=True, dict_save_path=""):
        doc_stream = (tokens for _, tokens in iter_news(self.path))
        self.dictionary = gensim.corpora.Dictionary(doc_stream)
        self.dictionary.filter_extremes(no_below=20, no_above=0.1)

        if save:
            self.dictionary.save(dict_save_path)
