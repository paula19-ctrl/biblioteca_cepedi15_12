from django.contrib import admin
from .models import Editora


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone')
    search_fields = ['nome']


from django.contrib import admin

# Register your models here.
