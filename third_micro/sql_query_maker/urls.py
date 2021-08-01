from django.urls import path

from sql_query_maker.api import SQLViewSet

urlpatterns = [
    path('make_file/', SQLViewSet.as_view({'post': 'retrieve'})),
]