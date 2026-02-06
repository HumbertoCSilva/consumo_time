from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Item(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao

class Lancamento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item)
    data_hora = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.funcionario.nome} - {self.data_hora.strftime('%d/%m %H:%M')}"