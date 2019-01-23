from django.urls import path
from . import views, apiviews
from .apiviews import ReportViewSet, ReportDetail

from rest_framework.routers import DefaultRouter

urlpatterns = [
    # views (url, file, function name)
    path('', views.index, name ='index'),
    path('training', views.training, name ='training'),
    path('detail/<int:report_id>/', views.detail, name='detail'),
    path('api/clf/', apiviews.clf)
]

# routing for apiviews
router = DefaultRouter()
router.register('api/reports', ReportViewSet, base_name="reports")

urlpatterns += router.urls
