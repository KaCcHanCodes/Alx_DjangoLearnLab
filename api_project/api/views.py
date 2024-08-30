from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

def BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer