from rest_framework.test import APIRequestFactory
# from .models import Book, Author
# from django.test import TestCase

# class BookTestCase(TestCase):
#     def setup(self):
#         Book.objects.create(title='Before The End',
#                             author='toryiama', 
#                             publication_date=2009
#                             )

factory = APIRequestFactory()
create_request = factory.post('/books/create/', {'title': 'Before The End', 'author': 'toryiama', 'publication_date': 2009})
update_request = factory.post('/books/update/', {'title': 'Before The End'})
delete_request = factory.post('/books/delete/', {'author': 'toryiama'})