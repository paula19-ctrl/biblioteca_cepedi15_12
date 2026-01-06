from django import forms
from django.forms import ModelForm, DateInput

from .models import  Livro


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'ano_publicacao': forms.DateInput(
                format=('%Y/%m/%d'),
                attrs={ 'type': 'date',
                        'class': 'form-control'}),
        }