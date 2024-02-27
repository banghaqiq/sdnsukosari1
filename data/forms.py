from django import forms
from .models import *

class DataGuruForm(forms.ModelForm):
    class Meta:
        model = DataGuru
        fields = '__all__'
        widget = {
            'image' : forms.Select(attrs={'class' : 'form-control'}),
            'nama' : forms.Select(attrs={'class' : 'form-control'}),
            'jabatan' : forms.Select(attrs={'class' : 'form-control'}),
        }