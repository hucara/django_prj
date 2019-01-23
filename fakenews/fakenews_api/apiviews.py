from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics, viewsets

from django.shortcuts import get_object_or_404

from .models import Report
from .serializers import ReportSerializer

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from joblib import dump, load

# Generic api views
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_serializer(self, instance=None, data=None, many=False, partial=False):
        serializer = super(ReportViewSet, self).get_serializer(instance=instance, data=data, many=True, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return serializer

class ReportDetail(generics.RetrieveDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

@api_view(['POST'])
def clf(request):
    print("Getting data")
    doc = request.data

    result = {}
    result['data'] = doc
    result['total'] = doc['title']+' '+doc['author']+doc['content']

    print("Loading classifier...")
    clf = load('fakenews_api/classifier/serialized_models/logreg.joblib')
    count_vectorizer = load('fakenews_api/classifier/serialized_models/count_vectorizer.joblib')
    tfidf = count_vectorizer.transform([result['total']])
    print("Predicted:")
    labels = clf.predict(tfidf)
    result['labels'] = labels
    return Response(result)
