from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Oficina(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ubicación = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('oficina-list')

class Asociado(models.Model):
    oficina = models.ForeignKey('Oficina', on_delete=models.PROTECT,related_name='get_oficina')
    cedula = models.CharField(primary_key=True, max_length=30)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    estado_civil = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    correo = models.CharField(max_length=50)
    genero = models.CharField(max_length=9)
    estado = models.CharField(max_length=20)
    sueldo = models.DecimalField(max_digits=10, decimal_places=3)
    tipo_titularidad = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    fecha_de_vinculación = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cedula
    
    def get_absolute_url(self):
        return reverse('asociados-list')
    
class Aporte(models.Model):
    id = models.AutoField(primary_key=True)
    asociado = models.ForeignKey('Asociado', on_delete=models.PROTECT,related_name='get_asociados')
    fecha = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return str(self.id) + " " + str(self.valor)
    
    def get_absolute_url(self):
        return reverse('aporte-list')