from rest_framework.test import APIRequestFactory, APITestCase
from .models import Book

class BookTestCase(APITestCase):
    def setup(self):
        Book.objects.create(title='Before The End',
                            author='toryiama', 
                            publication_date=2009
                            )

factory = APIRequestFactory()
create_request = factory.post('/books/create/', {'title': 'Before The End', 'author': 'toryiama', 'publication_date': 2009})
update_request = factory.post('/books/update/', {'title': 'Before The End'})
delete_request = factory.post('/books/delete/', {'author': 'toryiama'})