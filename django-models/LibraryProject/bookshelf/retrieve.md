from bookshelf.models import Book

#retrieves all instances in the database
all_entries = Book.objects.get(title="1984")
python(all_entries)