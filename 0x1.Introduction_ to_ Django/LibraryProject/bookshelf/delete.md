from bookshelf.model import Book

#Delete book by author
rm_book = Book.objects.filter(author=“George Orwell”)
rm_book.delete()