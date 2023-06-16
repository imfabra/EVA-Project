from django.db import models


# Create your models here.
class Etiquetas(models.Model):
    id_etiqueta = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)


    def __str__(self):
        return self.nombre


class Movimientos(models.Model):
    id_movimieto = models.BigAutoField(primary_key=True),
    # id_etiqueta = models.ForeignKey(Etiquetas, on_delete=models.CASCADE, verbose_name="Etiqueta relacionada")
    etiquetas = models.ManyToManyField(Etiquetas, related_name='movimientos')
    descripcion = models.CharField(max_length=45)
    orden = models.IntegerField()

    def __str__(self):
        return self.descripcion, self.orden


class Submovimientos(models.Model):
    id_submovimiento = models.BigAutoField(primary_key=True)
    id_movimiento = models.ForeignKey(Movimientos, on_delete=models.CASCADE, verbose_name="Movimiento relacionado", default=1)
    # id_movimiento = models.ManyToManyField(Movimientos, verbose_name="Movimiento relacionado", default=1)
    join_1 = models.DecimalField(max_digits=10, decimal_places=2)
    join_2 = models.DecimalField(max_digits=10, decimal_places=2)
    join_3 = models.DecimalField(max_digits=10, decimal_places=2)
    join_4 = models.DecimalField(max_digits=10, decimal_places=2)
    join_5 = models.DecimalField(max_digits=10, decimal_places=2)
    velocidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        data = list()
        data.append(self.join_1)
        data.append(self.join_2)
        data.append(self.join_3)
        data.append(self.join_4)
        data.append(self.join_5)
        data.append(self.velocidad)
        return data
