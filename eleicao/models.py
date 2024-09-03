from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Partido(models.Model):
    sigla = models.CharField(max_length=10)

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)