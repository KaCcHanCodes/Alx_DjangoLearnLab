from models import Librarian, Library, Book, Author

writer1 = Author(name="Amanda Okoro")
writer1.save()
writer2 = Author(name="John Bellossi")
writer2.save()

book1 = Book(title="The Becoming")
book1.save()
book2 = Book(title="Gotham Arises")
book2.save()

book_1 = Book.object.get(pk=1)
author1 = Author.object.get(name="Amanda Okoro")
book_1.author = author1
book_1.save()
book_2 = Book.object.get(pk=2)
author2 =Author.object.get(name="John Bellossi")
book_2.author = author2
book_2.save()

NY_Lib = Library(name="New York Library")
Enu_Lib = Library(name="Enugu Library")

#Query all books by a specific author
q1 = Book.object.filter(author="Amanda Okoro")
#list all books in the library
q2 = Library.object.all()
#Retrieve the librarian for a library.
q3 = Librarian.object.filter(library ="New York Library")