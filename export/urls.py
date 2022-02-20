from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchReport.as_view(), name='export_search_report'),
    path('download/file', views.download, name='download_report_file'),
]
