from django.core.validators import FileExtensionValidator
from django.forms import Form, CharField, TextInput, FileField, FileInput


class SearchEntityForm(Form):
    """
    Ricerca di una pratica
    """

    search = CharField(label="Digita l'entità da ricercare",
                       widget=TextInput(attrs={'id': 'search', 'name': 'search', 'class':'form-control',
                                               'placeholder': "Entità da cercare"
                                               }),
                       required=True,
                       error_messages={'required': 'Campo obbligatorio'})


class JSONtoSQL(Form):
    file_upload = FileField(widget=FileInput(attrs={'id': 'file_upload', 'name': 'file_upload', 'class': 'upload',
                                                    'accept': 'application/json'}),
                            validators=[FileExtensionValidator(['json'])],
                            error_messages={'validators': 'Caricare un file .json valido'},
                            label='Upload JSON',
                            required=True)
