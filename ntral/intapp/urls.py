from django.urls import path
from . import views, apiviews


urlpatterns = [
    # views (url, file, function name)
    path('', views.index, name='index'),
    path('api/search/', apiviews.search)
]
