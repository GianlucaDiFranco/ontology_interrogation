from rest_framework import viewsets

from sql_query_maker.tools import make_sql_query


class SQLViewSet(viewsets.ViewSet):

    def retrieve(self, request):
        """

        json_name: Nome del file.sql da generare
        json: file .json
        isolated_properties: bool per la creazione di tabelle separate relative alle proprietà
        return: query .sql
        """
        json_file_name = request.POST.get('sql_file_name')
        json_content = request.POST.get('json')
        print(request.POST.get('isolated_properties'))
        isolated_properties = request.POST.get('isolated_properties').lower() == 'true'
        data = make_sql_query(json_content, json_file_name, isolated_properties)
        return data
