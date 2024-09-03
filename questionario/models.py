from django.db import models

# Create your models here.

class Alternativa(models.Model):
    opcao = models.CharField(max_length=200)

    def __str__(self):
        return self.opcao

    class Meta:
        verbose_name = "Alternativa"

class Questao(models.Model):
    pergunta = models.CharField(max_length=200)    
    alternativas = models.ForeignKey(Alternativa, on_delete=models.CASCADE)

    def __str__(self):
        return self.pergunta
    class Meta:
        verbose_name = "Questõe"

class Livro(models.Model):
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Veiculo(models.Model):
    fabricante = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    placa = models.CharField(max_length=9)
    ano = models.DateField()

    def __str__(self):
       return self.modelo

class Teste(models.Model):
    pass