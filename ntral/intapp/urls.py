from django.urls import path
from . import views, apiviews
from .apiviews import ReportViewSet

from rest_framework.routers import DefaultRouter


urlpatterns = [
    # views (url, file, function name)
    path('', views.index, name='index'),
    path('api/search/', apiviews.search)
]
