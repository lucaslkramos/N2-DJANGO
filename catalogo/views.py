from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Jogo
from .forms import JogoForm, AvaliacaoForm


def pagina_inicial(request):
    jogo_destaque = Jogo.objects.filter(destaque=True).first()
    jogos = Jogo.objects.all().order_by('nome')
    if jogo_destaque:
        jogos = jogos.exclude(pk=jogo_destaque.pk)
    return render(request, 'catalogo/index.html', {
        'jogo_destaque': jogo_destaque,
        'jogos': jogos,
    })


def detalhe_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    form = AvaliacaoForm()
    return render(request, 'catalogo/detalhe_jogo.html', {'jogo': jogo, 'form': form})


def avaliar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.jogo = jogo
            avaliacao.save()
    return redirect('catalogo:detalhe_jogo', pk=jogo.pk)


@login_required()
def dashboard(request):
    jogos = Jogo.objects.all().order_by('nome')
    return render(request, 'catalogo/dashboard.html', {'jogos': jogos})


@login_required()
def novo_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:dashboard')
    else:
        form = JogoForm()
    return render(request, 'catalogo/jogo_form.html', {'form': form})


@login_required()
def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('catalogo:dashboard')
    else:
        form = JogoForm(instance=jogo)
    return render(request, 'catalogo/jogo_form.html', {'form': form})


@login_required()
def apagar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('catalogo:dashboard')
    return render(request, 'catalogo/jogo_confirmar_exclusao.html', {'jogo': jogo})
