from django import forms
from django.forms import ModelForm, DateInput

from .models import  Livro


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'ano_publicacao': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione uma data',
                       'type': 'date'
                       }),
        }