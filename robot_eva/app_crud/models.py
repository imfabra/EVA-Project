from django.db import models


# Esto define los modelos Etiqueta, Movimiento y Submovimiento con sus relaciones.
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class Submovimiento(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    join1 = models.DecimalField(max_digits=16, decimal_places=2)
    join2 = models.DecimalField(max_digits=16, decimal_places=2)
    join3 = models.DecimalField(max_digits=16, decimal_places=2)
    join4 = models.DecimalField(max_digits=16, decimal_places=2)
    join5 = models.DecimalField(max_digits=16, decimal_places=2)
    velocidad = models.DecimalField(max_digits=16, decimal_places=2)
    tiempo = models.DecimalField(max_digits=16, decimal_places=2)
    orden = models.IntegerField()

    def __str__(self):
        return f"Submovimiento {self.id}"
