import json

from django.http import HttpResponse

from tree_view.ont_interrogation_api import objects_api, subjects_api, property_values_api


def make_json(request):
    if request.method == "POST":
        elements = request.POST.copy()
        elements.pop('csrfmiddlewaretoken')
        file_name = elements.pop('json_name')[0]
        json_string = make_json_content(elements)
        return make_json_file(json_string, file_name)


def make_json_content(elements):
    fathers = []
    predicates = []
    properties = []
    # prendo padri e predicati
    for el in elements:
        if 'subClassOf' in el:
            fathers.append(el.split('_')[1])
        elif 'property' in el:
            properties.append(el.split('_')[1])
        else:
            predicates.append(el)


    # creo il dizionario prendendo tutti i figli dei padri (ovvero i fratelli della entity di partenza)
    father_dic = {}
    for father in fathers:
        sons = (subjects_api('subClassOf', father))
        son_dic = {}
        for son in sons:
            pred_dic = {}
            prop_dic = {}
            for p in predicates:
                pred_dic[p] = objects_api(son, p)
            for prop in properties:
                prop_dic[prop] = property_values_api(son, prop)
            son_dic[son] = {'predicates': pred_dic, 'properties': prop_dic}
        father_dic[father] = son_dic
        print(father_dic)
    return json.dumps(father_dic)


def make_json_file(json_string, file_name):
    response = HttpResponse()
    response['content_type'] = 'application/json'
    response['Content-Disposition'] = 'attachment; filename={}.json'.format(file_name)
    response.write(json_string)
    return response


def make_sql_file(json_string, file_name):
    response = HttpResponse()
    response['content_type'] = 'application/sql'
    response['Content-Disposition'] = 'attachment; filename={}.sql'.format(file_name)
    response.write(json_string)
    return response
