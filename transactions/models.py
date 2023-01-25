from django.db import models

class Transaction(models.Model):
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    donoLoja = models.CharField(max_length=14)
    nomeLoja = models.CharField(max_length=19)

