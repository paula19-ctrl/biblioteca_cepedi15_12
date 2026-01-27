from django.urls import path
from . import views


app_name = 'apps.editoras'

urlpatterns = [
    path('buscar_editoras/', views.buscar_editoras, name='buscar_editoras'),
    path('inserir_editora/', views.inserir_editora, name='inserir_editora'),
    path('listar_editoras/', views.listar_editoras, name='listar_editoras'),
    path('editar_editora/<int:id>/', views.editar_editora, name='editar_editora'),

]