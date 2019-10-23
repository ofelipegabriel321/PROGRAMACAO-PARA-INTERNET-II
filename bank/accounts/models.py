from django.db import models

class Accounts(models.Model):
    owner = models.CharField(max_length=200)
    balance = models.FloatField()
    creation_date = models.DateTimeField()

