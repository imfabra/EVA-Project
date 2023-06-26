from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Puntos(models.Model):
    id_punto = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    angulo1 = models.FloatField()
    angulo2 = models.FloatField()
    angulo3 = models.FloatField()
    angulo4 = models.FloatField()
    angulo5 = models.FloatField()
    velocidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class SecuenciaPuntos(models.Model):
    id_secuencia_puntos = models.CharField(max_length=50, primary_key=True)
    nombre_secuencia = models.CharField(max_length=50)
    punto1 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_puntos_punto1')
    punto2 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_puntos_punto2')
    punto3 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_puntos_punto3', null=True, blank=True)
    punto4 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_puntos_punto4', null=True, blank=True)
    punto5 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_puntos_punto5', null=True, blank=True)

    def __str__(self):
        return self.nombre_secuencia


class SecuenciaCombinada(models.Model):
    id_secuencia_combinada = models.CharField(max_length=50, primary_key=True)
    nombre_secuencia_combinada = models.CharField(max_length=50)
    pp1 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_combinada_pp1', null=True, blank=True)
    sp1 = models.ForeignKey(SecuenciaPuntos, on_delete=models.CASCADE, related_name='secuencia_combinada_sp1', null=True, blank=True)
    pp2 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_combinada_pp2', null=True, blank=True)
    sp2 = models.ForeignKey(SecuenciaPuntos, on_delete=models.CASCADE, related_name='secuencia_combinada_sp2', null=True, blank=True)
    pp3 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_combinada_pp3', null=True, blank=True)
    sp3 = models.ForeignKey(SecuenciaPuntos, on_delete=models.CASCADE, related_name='secuencia_combinada_sp3', null=True, blank=True)
    pp4 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_combinada_pp4', null=True, blank=True)
    sp4 = models.ForeignKey(SecuenciaPuntos, on_delete=models.CASCADE, related_name='secuencia_combinada_sp4', null=True, blank=True)
    pp5 = models.ForeignKey(Puntos, on_delete=models.CASCADE, related_name='secuencia_combinada_pp5', null=True, blank=True)
    sp5 = models.ForeignKey(SecuenciaPuntos, on_delete=models.CASCADE, related_name='secuencia_combinada_sp5', null=True, blank=True)

    def __str__(self):
        return self.nombre_secuencia_combinada
