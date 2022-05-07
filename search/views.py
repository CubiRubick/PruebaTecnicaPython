from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from porfolio.models import cliente
from search.serializers import ClientesSerializer

@api_view(['GET', 'POST'])
def client_list(request):
    """
    List all code Books, or create a new Book.
    """
    if request.method == 'GET':
        books = cliente.objects.all()
        serializer = ClientesSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
