import json

import requests
from rest_framework.response import Response

from micro import settings
from sql_query_maker.tools import make_sql_file
from tree_view.classes.choices import EndpointSQL


def make_file_api(json_file_name, json_data, isolated_properties):
    """
    Ricerca l'entity in micro
    :param json_file_name:
    :param json_data:
    :return: dizionario con predicati e oggetti
    """
    json_dic = {
        'sql_file_name': json_file_name,
        'json': json.dumps(json_data),
        'isolated_properties': isolated_properties == 'on'
    }
    rec = requests.post(settings.SQL_MAKER_API_URL + EndpointSQL.MAKE_QUERY.value, data=json_dic)
    print(rec.content.decode())
    return make_sql_file(rec.content.decode(), json_file_name.split('.')[0])
