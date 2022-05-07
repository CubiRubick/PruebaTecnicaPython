from porfolio.models import cliente
from .serializers import PeliculaSerializer
from rest_framework import viewsets

class PeliculaViewSet(viewsets.ModelViewSet):
  queryset = cliente.objects.all()
  serializer_class = PeliculaSerializer