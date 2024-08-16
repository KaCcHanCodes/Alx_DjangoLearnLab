from bookshelf.models import Book

#Delete book by author
book = Book.objects.filter(author=“George Orwell”)
book.delete()