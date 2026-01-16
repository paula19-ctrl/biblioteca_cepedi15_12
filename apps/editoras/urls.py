from django.urls import path
from . import views


app_name = 'apps.editoras'

urlpatterns = [
    path('inserir_editora/', views.inserir_editora, name='inserir_editora'),
    path('listar_editoras/', views.listar_editoras, name='listar_editoras'),

]