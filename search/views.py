from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from porfolio.models import cliente
from search.serializers import ClientesSerializer

@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        Clientes = cliente.objects.all()
        serializer = ClientesSerializer(Clientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        clientes = cliente.objects.get(pk=pk)
    except cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientesSerializer(clientes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientesSerializer(clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
