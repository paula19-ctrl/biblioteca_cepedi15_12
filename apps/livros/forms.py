from django import forms
from django.forms import ModelForm, DateInput

from .models import  Livro


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'