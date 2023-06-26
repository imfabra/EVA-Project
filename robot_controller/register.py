from . import models

def register_model():
    # Registrar un punto
    punto_a = models.Puntos.objects.create(id_punto='P1', nombre='Punto A', angulo1=45, angulo2=30, angulo3=60, angulo4=90, angulo5=120, velocidad=5)
    punto_b = models.Puntos.objects.create(id_punto='P2', nombre='Punto B', angulo1=45, angulo2=30, angulo3=60, angulo4=90, angulo5=120, velocidad=5)
    punto_c = models.Puntos.objects.create(id_punto='P3', nombre='Punto C', angulo1=45, angulo2=30, angulo3=60, angulo4=90, angulo5=120, velocidad=5)

    # Registrar una secuencia de puntos
    secuencia_1 = models.SecuenciaPuntos.objects.create(id_secuencia_puntos='SP1', nombre_secuencia='Secuencia 1', punto1=punto_a, punto2=punto_b, punto3=punto_c)

    # Registrar una secuencia combinada
    secuencia_combinada_1 = models.SecuenciaCombinada.objects.create(id_secuencia_combinada='SC1', nombre_secuencia_combinada='Combinada 1', elemento1=punto_a.id_punto, elemento2=punto_b.id_punto)

    # Asignar una secuencia de puntos existente a una secuencia combinada
    secuencia_combinada_2 = models.SecuenciaCombinada.objects.create(id_secuencia_combinada='SC2', nombre_secuencia_combinada='Combinada 2', elemento1=secuencia_1.id_secuencia_puntos, elemento2=punto_c.id_punto)
