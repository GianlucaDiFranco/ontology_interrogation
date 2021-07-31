def get_name_from_URI(uri_string):
    """
    Rimuove il prefisso dall'uri
    :param uri_string: stringa dell'URI
    :return: testo dopo il cancelletto
    """
    split_string = uri_string.split("#", 1)
    return split_string[-1]


def get_bool_from_str(string_bool):
    return string_bool.lower() in ['true', '1', 't', 'y', 'yes'] if string_bool else True
