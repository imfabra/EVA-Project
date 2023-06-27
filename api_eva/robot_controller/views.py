from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
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
        #tasks.mov_zero.apply_async(args=())
        
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

# Vista de ejecucion de secuencias.
class SecuenciaPlayPuntosView(generics.CreateAPIView):
    serializer_class = serializer.SecuenciaPuntosSerializer
    queryset = models.SecuenciaPuntos.objects.all()

    def create(self, request, *args, **kwargs):
        secuencia_id = request.data.get('id_secuencia_puntos')

        try:
            secuencia_puntos = models.SecuenciaPuntos.objects.get(id_secuencia_puntos=secuencia_id)
        except models.SecuenciaPuntos.DoesNotExist:
            return self.get_response({'error': 'La secuencia no existe.'}, status=400)
        
        secuencia_data = serializer.SecuenciaPuntosSerializer(secuencia_puntos).data

        puntos_data = {}
        for i in range(1, 6):
            punto_id = secuencia_data[f'punto{i}']
            if punto_id is not None:
                try:
                    punto = models.Puntos.objects.get(id_punto=punto_id)
                    puntos_data[f'punto{i}'] = {
                        'ID': punto_id,
                        'puntos_data': {
                            'id_punto': punto.id_punto,
                            'nombre': punto.nombre,
                            'angulo1': punto.angulo1,
                            'angulo2': punto.angulo2,
                            'angulo3': punto.angulo3,
                            'angulo4': punto.angulo4,
                            'angulo5': punto.angulo5,
                            'velocidad': punto.velocidad,
                        },
                    }
                except models.Puntos.DoesNotExist:
                    return self.get_response({'error': f'El punto {punto_id} no existe.'}, status=400)

        full_data = {
            'message': '¡Operación ejecutada - exitosa!',
            'status': 'ok',
            'id_secuencia': secuencia_data['id_secuencia_puntos'],
            'nombre_secuencia': secuencia_puntos.nombre_secuencia,
            'secuencia_puntos': puntos_data,
        }

        tasks.sep_eva.apply_async(kwargs=full_data)

        return self.get_response(full_data)
    
    def get_response(self, data, status=200):
        return Response(data, status=status)
