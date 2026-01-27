
from django.shortcuts import render
from apps.alunos.models import Aluno
from apps.livros.models import Livro
from apps.emprestimos.models import Emprestimo

def index(request):
    context = {
        'qtd_alunos': Aluno.objects.count(),
        'qtd_livros': Livro.objects.count(),
        'qtd_emprestimos': Emprestimo.objects.count(),
    }
    return render(request, 'core/index.html')


def configuracao(request):
    return render(request, "core/configuracao.html")