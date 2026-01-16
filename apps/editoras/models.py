from django.db import models
from datetime import date


class Editora(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=False, null=False)


    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Editora'
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['nome']


from django.db import models

# Create your models here.
