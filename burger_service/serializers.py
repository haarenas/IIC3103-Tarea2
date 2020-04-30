from rest_framework import serializers
from . models import Hamburguesa, Ingrediente

class hamburguesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
        read_only_fields = ['id', 'ingredientes']

class ingredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']
        read_only_fields = ['id']