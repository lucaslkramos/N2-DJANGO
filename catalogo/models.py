from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    data_lancamento = models.DateField()
    destaque = models.BooleanField(default=False)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    plataformas = models.ManyToManyField(Plataforma)
    foto = models.ImageField(upload_to='fotos_jogos/', blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'


class Avaliacao(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='avaliacoes')
    nome_visitante = models.CharField(max_length=100)
    nota = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField()

    def __str__(self):
        return f'{self.nome_visitante} - {self.jogo.nome}'
