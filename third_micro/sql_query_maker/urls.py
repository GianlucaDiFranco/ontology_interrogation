from django.urls import path

from third_micro.sql_query_maker.api import SQLViewSet

urlpatterns = [
    path('make_file/', SQLViewSet.as_view({'post': 'retrieve'})),
]