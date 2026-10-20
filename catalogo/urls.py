from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('jogos/<int:pk>/', views.detalhe_jogo, name='detalhe_jogo'),
    path('avaliar/<int:pk>/', views.avaliar_jogo, name='avaliar_jogo'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('jogos/novo/', views.novo_jogo, name='novo_jogo'),
    path('jogos/<int:pk>/editar/', views.editar_jogo, name='editar_jogo'),
    path('jogos/<int:pk>/apagar/', views.apagar_jogo, name='apagar_jogo'),
]
