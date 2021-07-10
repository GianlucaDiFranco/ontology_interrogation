from django.template.defaulttags import register

@register.filter
def get_item(dictionary):

    return dictionary.pop()
