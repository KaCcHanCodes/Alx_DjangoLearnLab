from bookshelf.models import Book

#Creating a new book
book_1 = Book.objects.create(title="1984", author=“George Orwell”, publication_year=1949)
book_1.save()