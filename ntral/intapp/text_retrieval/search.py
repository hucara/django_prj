import json
import os


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
        print(self.index)
        print(os.getcwd())
        return self.index[vec_lsi]

    def _rank_by_similarity(self, query_result):
        res_sorted = sorted(enumerate(query_result), key=lambda item: -item[1])
        return res_sorted

    def _get_file_lines(self, sim_rank):
        sim_ids = [i[0] for i in sim_rank]

        fp = open(self.path)
        result = []
        for line_idx, line in enumerate(fp):
            if line_idx in sim_ids:
                sim_idx = sim_ids.index(line_idx)
                sim_val = sim_rank[sim_idx]
                line = json.loads(line)
                result.append(
                    (sim_val, line['headline'], line['short_description'])
                )

        result.sort(key=lambda tup: tup[0][1], reverse=True)
        return result

    def query(self, query, num_results=1, return_id=False):
        vec_lsi = self._transform_query(query)
        res = self._query_index(vec_lsi)
        res = self._rank_by_similarity(res)

        if return_id:
            return res[:num_results]
        else:
            return self._get_file_lines(res[:num_results])
