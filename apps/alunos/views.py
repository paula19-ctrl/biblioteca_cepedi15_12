from django.contrib import messages

from .forms import AlunoForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Aluno
from django.db.models.functions import Lower

from django.http import JsonResponse


def inserir_aluno(request):
    template_name = 'alunos/form_aluno.html'
    if request.method == 'POST':
        form = AlunoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'O Aluno salvo com sucesso.')
            return redirect('alunos:listar_alunos')
    form = AlunoForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_alunos(request):
    ordens = {
        'nome_asc': Lower('nome'),
        'nome_desc': Lower('nome').desc(),

        'id_asc': 'id',
        'id_desc': '-id',

        'matricula_asc': 'matricula',
        'matricula_desc': '-matricula',

        'data_evento_asc': 'data_evento',
        'data_evento_desc': '-data_evento',
    }

    ordem = request.GET.get('ordem', 'nome_asc')
    ordem_db = ordens.get(ordem, Lower('nome'))

    alunos = (
        Aluno.objects
        .all()
        .order_by(ordem_db)
    )

    return render(request, 'alunos/listar_alunos.html', {
        'alunos': alunos,
        'ordem': ordem,
    })

def editar_alunos(request, id):
    template_name = 'alunos/form_aluno.html'
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('alunos:listar_alunos')
    return render(request, template_name, context)

def excluir_aluno(request, id):
    template_name = 'alunos/excluir_aluno.html'
    aluno = Aluno.objects.get(id=id)
    context = {'aluno': aluno}
    if request.method == "POST":
        aluno.delete()
        messages.error(request, 'O Aluno foi excluído com sucesso!')
        return redirect('alunos:listar_alunos')
    return render(request, template_name, context)


def buscar_alunos(request):
    termo = request.GET.get('q', '')
    alunos = Aluno.objects.filter(nome__icontains=termo)[:10]
    resultados = [{'id': a.id, 'text': a.nome} for a in alunos]  # text aqui
    return JsonResponse(resultados, safe=False)