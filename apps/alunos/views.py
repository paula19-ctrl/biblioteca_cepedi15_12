from django.contrib import messages

from .forms import AlunoForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Aluno

from django.db.models.functions import Lower

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
    template_name = 'alunos/listar_alunos.html'

    ordem = request.GET.get('ordem', 'nome_asc')  # padrão

    if ordem == 'nome_asc':
        alunos = Aluno.objects.all().order_by(Lower('nome'))
    elif ordem == 'nome_desc':
        alunos = Aluno.objects.all().order_by(Lower('nome').desc())
    elif ordem == 'id_asc':
        alunos = Aluno.objects.all().order_by('id')
    elif ordem == 'id_desc':
        alunos = Aluno.objects.all().order_by('-id')
    elif ordem == 'matricula_asc':
        alunos = Aluno.objects.all().order_by('matricula')
    elif ordem == 'matricula_desc':
        alunos = Aluno.objects.all().order_by('-matricula')
    elif ordem == 'data_evento_asc':
        alunos = Aluno.objects.all().order_by('data_evento')
    elif ordem == 'data_evento_desc':
        alunos = Aluno.objects.all().order_by('-data_evento')

    else:
        alunos = Aluno.objects.all().order_by(Lower('nome'))  # fallback

    context = {
        'alunos': alunos,
        'ordem': ordem,
    }
    return render(request, template_name, context)

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
