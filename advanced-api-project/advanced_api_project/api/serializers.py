from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['title', 'publication_year', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    name = BookSerializer(source='book.title', read_only=True)

    class Meta:
        model = Author
        field = ['name']