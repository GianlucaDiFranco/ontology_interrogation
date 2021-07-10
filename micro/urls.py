from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path('agency/api/', include('agency.urls')),
    path('sql/api/', include('sql_query_maker.urls')),
    path('tree_view/', include('tree_view.urls'))
]
