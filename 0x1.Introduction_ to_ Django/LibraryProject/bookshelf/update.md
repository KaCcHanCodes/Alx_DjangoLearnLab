from bookshelf.model import Book

#Update a Book title
book = Book.objects.filter(title="1987")
book.title = "Nineteen Eighty-Four"
movify_db.save()