from datetime import datetime
from django.db import models

# Create your models here.
class Site(models.Model):
    nomeCliente = models.CharField(max_length=45)
    endereco =  models.CharField(max_length=45)
    CPF = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()