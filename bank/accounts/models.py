from django.db import models

class Account(models.Model):
    owner = models.CharField(max_length=200)
    balance = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('owner',)
