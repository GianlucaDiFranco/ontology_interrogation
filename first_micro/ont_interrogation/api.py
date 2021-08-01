from rest_framework import viewsets, status
from rest_framework.response import Response

from ont_interrogation.tools import get_predicate_object, get_objects, get_outgoing_predicates, get_subjects, get_properties, \
    get_property_values, get_prop_and_values


class SubjectViewSet(viewsets.ViewSet):

    def retrieve(self, request, predicate=None, object=None):
        """
        Dato predicato e oggetto, restituisce soggetti
        """
        if not object or not predicate:
            return Response("Soggetto o predicato non presenti", status=status.HTTP_404_NOT_FOUND)

        data = get_subjects(predicate, object)
        return Response(data, status=status.HTTP_200_OK)


class ObjectViewSet(viewsets.ViewSet):

    def retrieve(self, request, subject=None, predicate=None):
        """
        Dato soggetto e predicato, restituisco oggetti
        """
        if not subject or not predicate:
            return Response("Soggetto o predicato non presenti", status=status.HTTP_404_NOT_FOUND)

        data = get_objects(subject, predicate)
        return Response(data, status=status.HTTP_200_OK)


class PredicateViewSet(viewsets.ViewSet):

    def retrieve(self, request, subject=None, with_subclassof=None):
        """
        Dato soggetto e booleano che indica se inserire subclassof tra i predicati o escluderlo, restituisco predicati uscenti
        """
        if not subject:
            return Response("Soggetto non presente", status=status.HTTP_404_NOT_FOUND)

        data = get_outgoing_predicates(subject, with_subclassof if with_subclassof else True)
        return Response(data, status=status.HTTP_200_OK)


class PredObjViewSet(viewsets.ViewSet):

    def retrieve(self, request, entity=None):
        """
        Data una entity, restituisce un dizionario con predicati e oggetti
        """
        if not entity:
            return Response("Nessuna entity presente", status=status.HTTP_404_NOT_FOUND)
        data = get_predicate_object(entity.capitalize())
        return Response(data, status=status.HTTP_200_OK)


class PropertyViewSet(viewsets.ViewSet):

    def retrieve(self, request, entity=None):
        """
        Data una entity, restituisce le relative proprietà
        """
        if not entity:
            return Response("Nessuna entity presente", status=status.HTTP_404_NOT_FOUND)
        data = get_properties(entity.capitalize())
        return Response(data, status=status.HTTP_200_OK)


class PropertyValueViewSet(viewsets.ViewSet):

    def get_values(self, request, subject=None, property=None):
        """
        Dato soggetto e una proprietà, restituisco il valore delle proprietò
        """
        if not subject or not property:
            return Response("Soggetto o property non presenti", status=status.HTTP_404_NOT_FOUND)

        data = get_property_values(subject, property)
        return Response(data, status=status.HTTP_200_OK)

    def get_prop_and_values(self, request, subject=None):
        """
        Dato il soggetto, restituisco proprietà e relativi valori
        """
        if not subject:
            return Response("Soggetto o property non presenti", status=status.HTTP_404_NOT_FOUND)

        data = get_prop_and_values(subject)
        return Response(data, status=status.HTTP_200_OK)


