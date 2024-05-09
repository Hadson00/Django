from datetime import datetime
from django.db import models

# Create your models here.
class Site(models.Model):
    idCliente = models.CharField(max_length=100)
    nome =  models.CharField(max_length=45)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=45)
    telefone = models.CharField(max_length=11)
    dataNascimento = models.DateField()
    email = models.EmailField()