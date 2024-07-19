from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']



class CodeSearchForm(forms.Form):
    code = forms.CharField(max_length=8, label='Enter Code')


class ExpiringFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'expiration_date']