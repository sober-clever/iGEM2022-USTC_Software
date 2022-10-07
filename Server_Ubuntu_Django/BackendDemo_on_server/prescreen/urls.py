from django.urls import path
from .views import query_list, sencond_query

app_name = 'prescreen'

urlpatterns = [
    path('query', query_list, name='query'),
    path('second_query', sencond_query, name='second_query')
]
