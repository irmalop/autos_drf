from rest_framework import serializers
from .models import Marca, Auto

class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Auto
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['marca'] = MarcaSerializer(instance.marca).data        
        return response