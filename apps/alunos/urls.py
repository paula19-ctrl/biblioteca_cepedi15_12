from django.urls import path
from . import views


app_name = 'apps.alunos'

urlpatterns = [
    path('buscar_alunos/', views.buscar_alunos, name='buscar_alunos'),
    path('inserir_aluno/', views.inserir_aluno, name='inserir_aluno'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
    path('editar_aluno/<int:id>/', views.editar_alunos, name='editar_aluno'),
    path('excluir_aluno/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]