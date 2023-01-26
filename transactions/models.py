from django.db import models

class Transaction(models.Model):
    type_transaction = models.IntegerField()
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()

    store = models.ForeignKey(
        'stores.Store',
        on_delete = models.CASCADE,
        related_name = 'transactions'
    )

