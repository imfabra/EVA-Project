from rest_framework import serializers
from . import models

# serializa de python a json
class PuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Puntos
        fields = ('__all__')

class SecuenciaPuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SecuenciaPuntos
        fields = ('__all__')

class SecuenciaCombinadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SecuenciaCombinada
        fields = ('__all__') 