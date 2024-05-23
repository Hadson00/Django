from django.db import models

# Create your models here.

class Curso(models.Model):
    nomeCurso = models.CharField(max_length=45)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tempo = models.IntegerField(help_text='Tempo de duração: ')
    path = models.ImageField(upload_to='imagens/')