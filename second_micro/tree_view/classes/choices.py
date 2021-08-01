from enum import Enum


class EndpointOntInterrogation(Enum):
    SEARCH = 'predicate_obj/'
    SUBJECTS = 'subjects/'
    PREDICATES = 'predicates/'
    OBJECTS = 'objects/'
    PROPERTIES = 'properties/'
    PROPERTY_VALUES = 'property_values/'


class EndpointSQL(Enum):
    MAKE_QUERY = 'make_file/'
