from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    precio = models.DecimalField(decimal_places=2, max_digits=8)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

# Create your models here.
