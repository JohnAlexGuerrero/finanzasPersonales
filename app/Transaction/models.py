from django.db import models
from django.urls import reverse
from django.db.models import Sum, Count

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=150, null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Expense(Transaction):
    class TypeExpense(models.TextChoices):
        ALIMENTACION = "Alimentacion"
        TRANSPORTE = "Transporte"
        ALOJAMIENTO = "Alojamiento"
        ENTRETENIMIENTO = "Entretenimiento"
        SALUD = "Salud"
        EDUCACION = "Educación"
        INPUESTOS = "Impuestos"
        SEGUROS = "Seguros"
        SERVICIOS_PUBLICOS = "Servicios públicos"
        MANTENIMIENTO = "Mantenimiento"
        MODA = "Moda"
        TEXNOLOGIA = "Tecnología"
        REGALOS = "Regalos"
        VIAJES = "Viajes"
    
    type = models.CharField(max_length=150, choices=TypeExpense.choices)
    
    class Meta:
        verbose_name = ("Expense")
        verbose_name_plural = ("Expenses")    

    def __str__(self):
        return self.type
    
    def category(self):
        data = {"name":self.type, "total": self.total_value_by_type(), "number": self.number_transactions_by_type()}
        return data
    
    def total_value_by_type(self):
        return Expense.objects.filter(type=self.type).aggregate(Sum('value'))['value__sum']
    
    def number_transactions_by_type(self):
        return Expense.objects.filter(type=self.type).aggregate(Count('id'))['id__count']

class Income(Transaction):
    class TypeIncome(models.TextChoices):
        SALARIO = "Salario"
        BONIFICACION = "Bonificacion"
        ALQUILER = "Alquileres"
        INTERESES = "Intereses"
        GANACIAS = "Ganancias"
        PENSION = "Pension"
        HERENCIA = "Herencia"
        VENTAS = "Ventas"
        SUBSIDIOS = "Subsidios"

    type = models.CharField(max_length=150, choices=TypeIncome.choices)
    
    class Meta:
        verbose_name = ("Income")
        verbose_name_plural = ("Incomes")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("Income_detail", kwargs={"pk": self.pk})
