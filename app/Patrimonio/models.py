from django.db import models
from django.urls import reverse

# Create your models here.

class Patrimonio(models.Model):
    description = models.CharField(max_length=150, null=True, blank=True)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_fijo = models.BooleanField()
    created = models.DateField(auto_now_add=False)
    updated = models.DateField(auto_now_add=True)
    

    class Meta:
        abstract = True

class Active(Patrimonio):
    class Category(models.TextChoices):
        INVENTARIOS = "Inventarios"
        PROPIEDADES = "Propiedades"
        EQUIPO = "Equipo"
        VEHICULOS = "Vehiculos"
        AHORRO = "Ahorros"
        TITULOS_VALOR = "Titulos de Valor"
        
    class Type(models.TextChoices):
        TANGIBLE = "Tangibles"
        IN_TANGIBLE = "No Tangibles"
        
    type = models.CharField(max_length=150, choices=Type.choices)
    category = models.CharField(max_length=150, choices=Category.choices)

    class Meta:
        verbose_name = ("Active")
        verbose_name_plural = ("Actives")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Active_detail", kwargs={"pk": self.pk})
    
    def showCategories(self):
        return [x[0] for x in self.category]


class Passive(Patrimonio):
    class Category(models.TextChoices):
        CREDITO = "Creditos"
        PROVEEDORES = "Proveedores"
        EQUIPO = "Equipo"
        VEHICULOS = "Vehiculos"
        PROPIEDADES = "Propiedades"
        
    class Type(models.TextChoices):
        TANGIBLE = "Tangibles"
        IN_TANGIBLE = "No Tangibles"
        
    type = models.CharField(max_length=150, choices=Type.choices)
    category = models.CharField(max_length=150, choices=Category.choices)

    class Meta:
        verbose_name = ("Passive")
        verbose_name_plural = ("Passive")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Active_detail", kwargs={"pk": self.pk})
