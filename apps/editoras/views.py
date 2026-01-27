from django.contrib import messages
from django.db.models.functions import Lower
from .forms import EditoraForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Editora

from django.http import JsonResponse

def inserir_editora(request):
    template_name = 'editoras/form_editora.html'
    if request.method == 'POST':
        form = EditoraForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do editora foi realizado com sucesso!')
        return redirect('editoras:listar_editoras')
    form = EditoraForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_editoras(request):
    template_name = 'editoras/listar_editoras.html'

    ordens = {
        'id_asc': 'id',
        'id_desc': '-id',

        'nome_asc': Lower('nome'),
        'nome_desc': Lower('nome').desc(),

    }

    ordem = request.GET.get('ordem', 'id_asc')
    ordem_db = ordens.get(ordem, 'id')

    editoras = Editora.objects.all().order_by(ordem_db)

    return render(request, template_name, {
        'editoras': editoras,
        'ordem': ordem,
    })

def editar_editora(request, id):
    template_name = 'editoras/form_editora.html'
    editora = get_object_or_404(Editora, id=id)
    form = EditoraForm(request.POST or None, request.FILES or None, instance=editora)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('editoras:listar_editoras')
    return render(request, template_name, context)


def buscar_editoras(request):
    termo = request.GET.get('q', '')
    editoras = Editora.objects.filter(nome__icontains=termo)[:10]
    resultados = [{'id': e.id, 'text': e.nome} for e in editoras]  # text aqui
    return JsonResponse(resultados, safe=False)