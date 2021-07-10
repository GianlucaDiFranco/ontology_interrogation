from django.urls import path

from agency.api import PredObjViewSet, ObjectViewSet, PredicateViewSet, SubjectViewSet, PropertyViewSet, \
    PropertyValueViewSet

urlpatterns = [
    path('predicate_obj', PredObjViewSet.as_view({'get': 'list'})),
    path('predicate_obj/<str:entity>', PredObjViewSet.as_view({'get': 'retrieve'})),

    path('objects/<str:subject>/<str:predicate>', ObjectViewSet.as_view({'get': 'retrieve'})),
    path('subjects/<str:predicate>/<str:object>', SubjectViewSet.as_view({'get': 'retrieve'})),

    path('predicates/<str:subject>', PredicateViewSet.as_view({'get': 'retrieve'})),
    path('predicates/<str:subject>/<str:with_subclassof>', PredicateViewSet.as_view({'get': 'retrieve'})),

    path('properties/<str:entity>', PropertyViewSet.as_view({'get': 'retrieve'})),
    path('property_values/<str:subject>', PropertyValueViewSet.as_view({'get': 'get_prop_and_values'})),
    path('property_values/<str:subject>/<str:property>', PropertyValueViewSet.as_view({'get': 'get_values'})),
]
