from django.urls import path
from apps.livros import views


app_name = 'apps.livros'

urlpatterns = [
    path('inserir_livro/', views.inserir_livro, name='inserir_livro'),
    path('listar_livros/', views.listar_livros, name='listar_livros'),
    path('editar_livro/<int:id>/', views.editar_livro, name='editar_livro'),
    path('excluir_livro/<int:id>/', views.excluir_livro, name='excluir_livro'),
]