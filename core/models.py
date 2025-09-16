from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

# Modelo para o perfil do usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione aqui campos para configuracoes, como tema, moeda, etc.
    # Exemplo:
    # theme = models.CharField(max_length=10, default='light')
    # currency = models.CharField(max_length=3, default='BRL')

    def __str__(self):
        return f'{self.user.username} Profile'

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('IN', 'Entrada'),
        ('OUT', 'Saída'),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.description} - {self.amount}'

class SavingGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
