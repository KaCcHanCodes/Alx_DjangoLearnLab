from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

def BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer