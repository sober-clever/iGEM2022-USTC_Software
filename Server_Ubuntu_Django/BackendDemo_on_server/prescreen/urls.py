from django.urls import path
from .views import query_list

app_name = 'prescreen'

urlpatterns = [
    path('query', query_list, name='query'),
]
