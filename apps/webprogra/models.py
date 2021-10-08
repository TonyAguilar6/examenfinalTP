from django.db import models

# Create your models here.
class employee(models.Model):
    pk_employee = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50,  blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=False, null=False)
    date_bo = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=8,  blank=True, null=False)
    direcciono = models.TextField(blank=False, null=False)
    modelo = models.CharField(max_length=50, blank=False, null=False)
    marca = models.CharField(max_length=50, blank=False, null=False)
    ram = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
    rom = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)

