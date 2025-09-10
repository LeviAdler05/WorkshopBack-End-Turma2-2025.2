from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    localidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    ddd = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return f"{self.cep} - {self.logradouro}"