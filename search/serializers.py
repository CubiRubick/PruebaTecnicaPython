from porfolio.models import cliente
from rest_framework import serializers

class PeliculaSerializer(serializers.ModelSerializer):
  class Meta:
    model = cliente
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'