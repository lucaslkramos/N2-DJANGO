from django import forms
from .models import Jogo, Avaliacao

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'descricao', 'preco', 'data_lancamento', 'destaque', 'genero', 'plataformas', 'foto']
        widgets = {'data_lancamento': forms.DateInput(attrs={'type': 'date'})}


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nome_visitante', 'nota', 'comentario']
