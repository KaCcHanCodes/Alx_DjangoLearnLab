from django.db import models

class Author(models.model):
    name = models.CharField(max_length=100)

class Book(models.model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library')

class Librarian(models.model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)