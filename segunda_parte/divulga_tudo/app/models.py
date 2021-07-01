from django.db import models

class Anuncios(models.Model):
    nome_anuncio = models.CharField(blank=False, null=False, max_length=150);
    nome_cliente = models.CharField(blank=False, null=False, max_length=150);
    data_inicio = models.DateField(blank=False, null=False);
    data_fim = models.DateField(blank=False, null=False);
    investimento_dia = models.DecimalField(blank=False, null=False, max_digits=100, decimal_places=2);