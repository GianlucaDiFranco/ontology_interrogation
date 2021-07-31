import json
import requests
from second_micro import settings
from tree_view.classes.choices import EndpointAgency


def pred_obj_api(entity):
    """
    Ricerca l'entity in micro
    :param entity:
    :return: dizionario con predicati e oggetti
    """
    rec = requests.get(settings.AGENCY_API_URL + EndpointAgency.SEARCH.value + entity)
    print("pred_obj_api con entity {} ritorna {}".format(entity, str(rec.json())))
    return rec.json()


def predicates_api(subject, with_subclassof=True):
    """
    Ricerca l'entity in micro
    :param subject:
    :param with_subclassof:
    :return: dizionario con predicati e oggetti
    """
    rec = requests.get(settings.AGENCY_API_URL + EndpointAgency.PREDICATES.value + subject + '/' + str(with_subclassof))
    print("predicates_api con subject {} e with_subclassof {} ritorna {}".format(subject, with_subclassof,
                                                                                 str(rec.json())))
    return rec.json()


def objects_api(subject, predicate):
    """
    Ricerca l'entity in micro
    :param subject:
    :param predicate:
    :return: dizionario con predicati e oggetti
    """
    rec = requests.get(settings.AGENCY_API_URL + EndpointAgency.OBJECTS.value + subject + '/' + predicate)
    print("objects_api con subject {} e predicate {} ritorna {}".format(subject, predicate, str(rec.json())))
    print(str(rec.json()))
    return rec.json()


def subjects_api(predicate, obj):
    """
    Ricerca l'entity in micro
    :param subject:
    :param predicate:
    :return: dizionario con predicati e oggetti
    """
    rec = requests.get(settings.AGENCY_API_URL + EndpointAgency.SUBJECTS.value + predicate + '/' + obj)
    print("subjects_api con predicate {} e obj {} ritorna {}".format(predicate, obj, str(rec.json())))
    return rec.json()


def properties_api(entity):
    """
    Ricerca l'entity in micro
    :param subject:
    :param predicate:
    :return: dizionario con predicati e oggetti
    """
    rec = requests.get(settings.AGENCY_API_URL + EndpointAgency.PROPERTIES.value + entity)
    print("properties_api con entity {} ritorna {}".format(entity, str(rec.json())))
    return rec.json()


def properties_and_values_api(subject):
    """
    Ricerca l'entity in micro
    :param subject:
    :param predicate:
    :return: dizionario con predicati e oggetti
    """
    rec = requests.get(settings.AGENCY_API_URL + EndpointAgency.PROPERTY_VALUES.value + subject)
    print("properties_and_values_api con subject {} ritorna {}".format(subject, str(rec.json())))
    return rec.json()


def property_values_api(subject, property):
    """
    Ricerca l'entity in micro
    :param subject:
    :param predicate:
    :return: dizionario con predicati e oggetti
    """
    rec = requests.get(
        "{}{}{}/{}".format(settings.AGENCY_API_URL, EndpointAgency.PROPERTY_VALUES.value, subject, property))
    print("property_values_api con subject {} e property {} ritorna {}".format(subject, property, str(rec.json())))
    return rec.json()
