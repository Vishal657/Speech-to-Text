from django import forms
from .models import upload

class  forupload(forms.ModelForm):

    class Meta():
        model=upload
        fields = ['file']