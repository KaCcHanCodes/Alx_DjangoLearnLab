from bookshelf.model import Book

#Update a Book title
modify_db = Book.objects.filter(title="1987")
Modify_db.title = "Nineteen Eighty-Four"
movify_db.save()