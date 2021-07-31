from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path('ont_interrogation/api/', include('ont_interrogation.urls')),
]
