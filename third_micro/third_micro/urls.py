from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path('sql/api/', include('sql_query_maker.urls')),
]
