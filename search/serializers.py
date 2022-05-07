from porfolio.models import cliente
from rest_framework import serializers

class ClientesSerializer(serializers.ModelSerializer):
  class Meta:
    model = cliente
    fields = ['id', 'nombre', 'email', 'numeroT', 'descripcion']
    