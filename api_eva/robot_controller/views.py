from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializer
from . import models
from . import tasks


# Vistas para el CRUD de la base de datos
class PuntosView(viewsets.ModelViewSet):
    serializer_class = serializer.PuntosSerializer
    queryset = models.Puntos.objects.all()

class SecuenciaPuntosView(viewsets.ModelViewSet):
    serializer_class = serializer.SecuenciaPuntosSerializer
    queryset = models.SecuenciaPuntos.objects.all()

class SecuenciaCombinadaView(viewsets.ModelViewSet):
    serializer_class = serializer.SecuenciaCombinadaSerializer
    queryset = models.SecuenciaCombinada.objects.all()

# Vista de ejecución del cero
class GoZero(APIView):
    def get(self, request, *args, **kwargs):
        tasks.mov_zero.apply_async(args=())
        
        data = {'message': 'Go Zero'}
        return Response(data)

# Vistas de ejecucion de posiciones
class PuntoPlayPostView(APIView):
    def post(self, request):
        id_punto_post = request.data.get('id_punto')
        
        if id_punto_post is not None:
            try:
                # Realizar la consulta a la base de datos utilizando el ID
                punto = models.Puntos.objects.get(id_punto=id_punto_post)
    
                # Crear el diccionario con los datos encontrados
                datos = {
                    'id_punto': punto.id_punto,
                    'nombre': punto.nombre,
                    'angulo1': punto.angulo1,
                    'angulo2': punto.angulo2,
                    'angulo3': punto.angulo3,
                    'angulo4': punto.angulo4,
                    'angulo5': punto.angulo5,
                    'velocidad': punto.velocidad,
                }

                tasks.mov_eva.apply_async(kwargs=datos)
    
                return Response({'data': datos, 'message': 'La buena paa, esta funcionando'})
            except models.Puntos.DoesNotExist:
                return Response({'message': 'No se encontraron datos'}, status=404)
        else:
            return Response({'message': 'Se requiere proporcionar un ID válido'}, status=400)
