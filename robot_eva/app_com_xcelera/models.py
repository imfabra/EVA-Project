from django.db import models


# Create your models here.
class Etiquetas(models.Model):
    id_etiqueta = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)


class Movimientos(models.Model):
    id_movimieto = models.BigAutoField(primary_key=True),
    id_etiqueta = models.ForeignKey(Etiquetas, on_delete=models.CASCADE, verbose_name="Etiqueta relacionada")
    descripcion = models.CharField(max_length=45)
    orden = models.IntegerField()


class Submovimientos(models.Model):
    id_submovimiento = models.BigAutoField(primary_key=True)
    # id_movimiento = models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    id_movimiento = models.ManyToManyField(Movimientos, verbose_name="Movimiento relacionado")
    join_1 = models.DecimalField(max_digits=3, decimal_places=2)
    join_2 = models.DecimalField(max_digits=3, decimal_places=2)
    join_3 = models.DecimalField(max_digits=3, decimal_places=2)
    join_4 = models.DecimalField(max_digits=3, decimal_places=2)
    join_5 = models.DecimalField(max_digits=3, decimal_places=2)
    velocidad = models.DecimalField(max_digits=3, decimal_places=2)
