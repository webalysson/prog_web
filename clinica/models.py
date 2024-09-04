from django.db import models

# Create your models here.

class Consulta(models.Model):
    relato = models.CharField(max_length=500)
    receita = models.CharField(max_length=500)
    data = models.DateField()

    def __str__(self):
        return self.relato

class Medico(models.Model):
    crm = models.CharField(max_length=500)
    nome = models.CharField(max_length=500)
    especialidade = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Medicamento(models.Model):
    nome = models.CharField(max_length=500)
    validade = models.DateField()

    def __str__(self):
        return self.nome