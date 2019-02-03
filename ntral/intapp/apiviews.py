from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics, viewsets
from .models import Report, ReportEntry
from .serializers import ReportSerializer
from .text_retrieval.search import SearchEngine

from gensim.models.lsimodel import LsiModel
from gensim.similarities import MatrixSimilarity
from gensim.corpora import Dictionary

from joblib import load


class ReportViewSet(viewsets.ModelViewSet):
    queryset = ReportEntry.objects.all()
    serializer_class = ReportSerializer

    def get_serializer(self, instance=None, data=None, many=False,
                       partial=False):
        serializer = super(ReportViewSet, self).get_serializer(
            instance=instance, data=data, many=True, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return serializer

@api_view(['POST'])
def search(request):

    result = {}
    data = request.data

    lsi = LsiModel.load('./data/lsi_news.model')
    index = MatrixSimilarity.load('./data/lsi_news.index')
    dictionary = Dictionary.load('./data/news.dict')

    se = SearchEngine(
        model=lsi, index=index, dictionary=dictionary,
        file_path="./data/News_Category_Dataset_v2.json"
        )
    result['doc'] = se.query(query=data[0]['query'], num_results=data[0]['return'])
    return Response(result)
