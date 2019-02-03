import json


class SearchEngine():

    def __init__(self, file_path, model, index, dictionary):
        self.path = file_path
        self.model = model
        self.index = index
        self.dictionary = dictionary

    def _transform_query(self, query):
        vec_bow = self.dictionary.doc2bow(query.lower().split())
        vec_lsi = self.model[vec_bow]
        return vec_lsi

    def _query_index(self, vec_lsi):
        return self.index[vec_lsi]

    def _rank_by_similarity(self, query_result):
        return sorted(enumerate(query_result), key=lambda item: -item[1])

    def _get_file_lines(self, res):
        ids = [i[0] for i in res]

        fp = open(self.path)
        for i, line in enumerate(fp):
            if i in ids:
                line = json.loads(line)
                return (line['headline'], line['short_description'])

    def query(self, query, num_results=1, return_id=False):
        q = self._transform_query(query)
        res = self._query_index(q)
        res = self._rank_by_similarity(res)

        if return_id:
            return res[:num_results]
        else:
            if len(res) == 1:
                res = [res]

            self._get_file_lines(res)
