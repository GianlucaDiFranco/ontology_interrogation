import json

from django.shortcuts import render

# Create your views here.
from tree_view.agency_api import pred_obj_api, predicates_api, objects_api, properties_api
from tree_view.forms import SearchEntityForm, JSONtoSQL
from tree_view.sql_qm_api import make_file_api


def search_entity(request):
    context = {
        'form': SearchEntityForm,
        'form_file' : JSONtoSQL(),
    }
    if request.POST:
        form = SearchEntityForm(request.POST)
        if form.is_valid():
            predicates = predicates_api(request.POST.get('search', None), False)
            properties = properties_api(request.POST.get('search', None))
            fathers = objects_api(request.POST.get('search', None), 'subClassOf')
            context = {
                'form': form,
                'form_file': JSONtoSQL(),
                'predicates': predicates,
                'properties': properties,
                'fathers': fathers
            }
    return render(request, 'tree_view.html', context)


def make_sql_query(request):

    if request.method == 'POST':
        print(request.FILES)
        form = JSONtoSQL(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES
            json_string = json.load(file['file_upload'])
            response_sql = make_file_api(str(file['file_upload']), json_string, request.POST.get('isolated_properties', False))
            return response_sql
        else:
            print(form.errors)

    return render(request, 'tree_view.html', {})
