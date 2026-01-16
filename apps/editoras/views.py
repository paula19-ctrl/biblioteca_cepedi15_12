from django.contrib import messages

from .forms import EditoraForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Editora

from django.db.models.functions import Lower

def inserir_editora(request):
    template_name = 'editoras/form_editora.html'
    if request.method == 'POST':
        form = EditoraForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'O editora salvo com sucesso.')
            return redirect('editoras:listar_editoras')
    form = EditoraForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_editoras(request):
    template_name = 'editoras/listar_editoras.html'
    editoras = Editora.objects.all()
    context = {'editoras': editoras}
    return render(request, template_name, context)