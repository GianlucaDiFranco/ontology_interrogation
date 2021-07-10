import json
import re

from django.http import HttpResponse


def make_sql_query(json_input, file_name, isolated_properties):
    query = make_query(json_input, isolated_properties)
    return make_sql_file(query, file_name)


def create_table(json_dic, isolated_properties=False):
    try:
        table_name = list(json_dic)[0]
        main_table_query = "CREATE TABLE {} ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, ".format(table_name)
        other_tables_query = ''
        main_columns_string = '( '
        main_columns = []
        property_columns = []
        for key in json_dic[table_name].keys():
            main_columns = list(json_dic[table_name][key]['predicates'])
            property_columns = list(json_dic[table_name][key]['properties'])
            break
        if isolated_properties:
            for prop in property_columns:
                table_name = re.findall('[A-Z][^A-Z]*', prop)[0]
                other_tables_query += "CREATE TABLE {} ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(255) );".format(table_name)
        else:
            main_columns += property_columns

        for column in main_columns:
            main_table_query += "{} varchar(255), ".format(column)
            main_columns_string += "{}, ".format(column)
        main_table_query = main_table_query[:-2]
        main_columns_string = main_columns_string[:-2]
        main_table_query += ');'
        main_columns_string += ')'
        # print(main_table_query + other_tables_query)
        return main_table_query + other_tables_query, main_columns_string
    except:
        return ''


def populate_sql_values(dic, value_type):
    sql_string = ''
    for k in dic[value_type].keys():
        sql_string += "\""
        for elem in dic[value_type][k][:-1]:
            sql_string += "{},".format(elem)
        if len(dic[value_type][k]) > 0:
            sql_string += "{}\",".format(dic[value_type][k][-1])
        else:
            sql_string += "\","
    return sql_string


def make_query(json_input, isolated_properties=True):
    """
    Converte un JSON in una stringa sql con creazione tabella e inserimento record
    :param json_input: JSON da convertire
    :param isolated_properties: JSON da convertire
    :return: stringa sql per creazione tabella ed inserimento record
    """

    try:
        json_dic = json.loads(json_input)
        main_table_name = list(json_dic)[0]

        sql_query, main_columns_string = create_table(json_dic, isolated_properties)
        sql_prop_relation_query = ''

        # tables property
        if isolated_properties:
            prop_dic = {}
            for prop in json_dic[main_table_name][list(json_dic[main_table_name].keys())[0]]['properties']:
                prop_dic[prop] = {}
                sql_prop_relation_query += "CREATE TABLE {} ( " \
                                           "main_element_id int, prop_element_id int" \
                                           ");".format('_'.join([main_table_name, prop]))

        for index, key in enumerate(json_dic[main_table_name].keys()):
            sql_insert = "INSERT INTO {} {} VALUES (".format(main_table_name,main_columns_string)
            sql_values = populate_sql_values(json_dic[main_table_name][key], 'predicates')
            if not isolated_properties:
                sql_values += populate_sql_values(json_dic[main_table_name][key], 'properties')
            else:
                for property_name in json_dic[main_table_name][key]['properties'].keys():
                    for prop_value in json_dic[main_table_name][key]['properties'][property_name]:
                        if prop_value not in prop_dic[property_name].keys():
                            print(str(prop_dic[property_name].keys()))
                            sql_prop_relation_query += "INSERT INTO {} (name) VALUES (\"{}\");".format(
                                re.findall('[A-Z][^A-Z]*', property_name)[0], prop_value)
                            prop_dic[property_name][prop_value] = len(prop_dic[property_name].keys())+1
                        sql_prop_relation_query += "INSERT INTO {} VALUES (\"{}\", \"{}\");".format(
                            '_'.join([main_table_name, property_name]), index+1, prop_dic[property_name][prop_value])

            sql_values = sql_values[:-1]
            sql_insert += "{});".format(sql_values)
            sql_query += "{}".format(sql_insert)
        print(sql_query + sql_prop_relation_query)
        return sql_query + sql_prop_relation_query
    except:
        return ''


def make_sql_file(text, file_name):
    response = HttpResponse()
    response['content_type'] = 'application/sql'
    response['Content-Disposition'] = 'attachment; filename={}.sql'.format(file_name)
    response.write(text)
    return response
