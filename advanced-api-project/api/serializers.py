from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def validate(self, data):
        if data['publication_year'] > datetime.today():
            raise serializers.ValidationError("Publication year is not valid")

class AuthorSerializer(serializers.ModelSerializer):
    name = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']