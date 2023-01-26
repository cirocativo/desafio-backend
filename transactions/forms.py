from django import forms
from django import templatetags

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Arquivo CNAB')
    