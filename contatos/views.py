from django.shortcuts import render, redirect, get_object_or_404
from .models import Contato
from .forms import ContatoForm

def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista.html', {'contatos': contatos})

def criar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contatos')
    else:
        form = ContatoForm()
    return render(request, 'contatos/form.html', {'form': form})

def deletar_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    contato.delete()
    return redirect('lista_contatos')
