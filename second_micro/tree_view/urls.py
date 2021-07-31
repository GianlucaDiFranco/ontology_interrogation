from django.conf.urls import url
from django.urls import path

from tree_view import views, utils

app_name = 'tree_view'

urlpatterns = [

    url(r'^$', views.search_entity, name='search_entity'),
    url(r'^sql_query$', views.make_sql_query, name='sql_query'),
    url(r'^json_tree$', utils.make_json, name='json_tree'),
]
