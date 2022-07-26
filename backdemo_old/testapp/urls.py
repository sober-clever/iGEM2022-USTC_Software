from django.urls import path
from testapp import views


app_name = 'testapp'

urlpatterns = [
    path('article', views.article_list, name='list'),
    path('query', views.query_list, name='query'),
]
