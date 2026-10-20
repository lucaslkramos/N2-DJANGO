from django.contrib import admin
from .models import Genero, Plataforma, Jogo, Avaliacao

admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Jogo)
admin.site.register(Avaliacao)