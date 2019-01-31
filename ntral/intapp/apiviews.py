from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics, viewsets
from .models import Report, ReportEntry
from .serializers import ReportSerializer

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
