import rdflib
from rdflib import URIRef

from first_micro.ont_interrogation.choices import RdfsPrefixPredicate, SkosPrefixPredicate
from first_micro.ont_interrogation.utils import get_name_from_URI, get_bool_from_str
from first_micro import settings

g = rdflib.Graph()
g.parse(settings.OWL_FILE_NAME)


def get_outgoing_predicates(entity, with_subclassof):
    """
    Restituisce i predicati uscenti da un'entity
    :param entity: entità da interrogare
    :param with_subclassof: boolean per includere (o no) il predicato subClassOf
    :return: predicati uscenti da entity
    """

    uri = URIRef("{}{}".format(settings.ONTOLOGY_PREFIX, entity))
    try:
        predicates = g.predicates(uri)

        pred_array = []
        for p in predicates:
            if not get_bool_from_str(with_subclassof) and 'subClassOf' in p:
                continue
            if get_name_from_URI(p) not in pred_array:
                pred_array.append(get_name_from_URI(p))
    except:
        return []
    return pred_array


def get_subjects(predicate, obj):
    """
    Restituisce gli uri dei soggetti dell'object relativi ad un predicato
    :param object: entità da interrogare
    :param predicate: predicato entrante
    :return: soggetti raggiunti
    """

    try:
        if predicate in RdfsPrefixPredicate:
            prefix = settings.RDFS_PREFIX
        elif predicate in SkosPrefixPredicate:
            prefix = settings.SKOS_PREFIX
        else:
            prefix = settings.OWL_PREFIX

        uri_pred = URIRef("{}{}".format(prefix, predicate))
        uri_obj = URIRef("{}{}".format(settings.ONTOLOGY_PREFIX, obj))
        subjects = g.subjects(uri_pred, uri_obj)
        subj_array = []
        for s in subjects:
            subj_array.append(get_name_from_URI(s))
    except:
        return []
    return subj_array


def get_objects(entity, predicate):
    """
    Restituisce gli uri degli oggetti dell'entity relativi ad un predicato
    :param entity: entità da interrogare
    :param predicate: predicato uscente
    :return: oggetti raggiunti
    """
    try:
        if predicate in RdfsPrefixPredicate:
            prefix = settings.RDFS_PREFIX
        elif predicate in SkosPrefixPredicate:
            prefix = settings.SKOS_PREFIX
        else:
            prefix = settings.OWL_PREFIX

        uri_sub = URIRef("{}{}".format(settings.ONTOLOGY_PREFIX, entity))
        uri_pred = URIRef("{}{}".format(prefix, predicate))
        objects = g.objects(uri_sub, uri_pred)
        obj_array = []
        for o in objects:
            if type(o) != rdflib.term.BNode:
                obj_array.append(get_name_from_URI(o))
    except:
        return []
    return obj_array


def get_properties(entity):
    """
    Restituisce le prorietà dell'entity
    :param entity: entità da interrogare
    :return: prorietà dell'entity
    """
    try:
        query_raw = """
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX entity_prefix: <{prefix}>
                    select distinct ?property where{{
                    {{
                        ?property rdfs:domain ?class . 
                        entity_prefix:{subj} rdfs:subClassOf+ ?class.
                        }} UNION {{
                          ?property rdfs:domain entity_prefix:{subj}.
                        }}
                    }}
                    """.format(prefix=settings.ONTOLOGY_PREFIX, subj=entity)
        qres = g.query(query_raw)
        URIs = []
        for prop_dic in qres.bindings:
            URIs.append(get_name_from_URI(prop_dic['property']))
    except:
        return []
    return URIs


def get_property_values(entity, property):
    """
    Oggetti relativi ad una proprietà di un entity
    """
    query_raw = """
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX entity_prefix: <{prefix}>
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                SELECT ?x 
                WHERE {{
                   entity_prefix:{entity} rdfs:subClassOf+ [
                        a owl:Restriction ;
                        owl:onProperty entity_prefix:{property}; 
                        owl:someValuesFrom ?x
                    ]
                }}
                """.format(prefix=settings.ONTOLOGY_PREFIX, entity=entity, property=property)
    try:
        qres = g.query(query_raw)
        URIs = []
        for prop_dic in qres.bindings:
            URIs.append(get_name_from_URI(prop_dic['x']))
    except:
        return []
    return URIs


def get_predicate_object(entity):
    """
    Restituisce i predicati uscenti da un'entity e relative entità raggiunte
    :param entity: entità da interrogare
    :return: predicati e oggetti raggiunti
    """
    try:

        uri = URIRef("{}{}".format(settings.ONTOLOGY_PREFIX, entity))
        predicates_and_objects = g.predicate_objects(uri)
        po_dict = {}
        for p, o in predicates_and_objects:
            if get_name_from_URI(p) not in po_dict.keys():
                po_dict[get_name_from_URI(p)] = [get_name_from_URI(o)]
            else:
                po_dict[get_name_from_URI(p)].append(get_name_from_URI(o))

    except:
        return {}
    return po_dict


def get_prop_and_values(entity):
    try:
        properties = get_properties(entity)
        prop_and_values = {}
        for property in properties:
            prop_and_values[property] = get_property_values(entity, property)

    except:
        return {}
    return prop_and_values
