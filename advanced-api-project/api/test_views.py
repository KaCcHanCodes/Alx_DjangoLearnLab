from rest_framework.test import APIRequestFactory, APITestCase
from .models import Book
from rest_framework import status
from django.urls import reverse

class BookTestCase(APITestCase):
    '''Create a book instance'''
    def setup(self):
        Book.objects.create(title='Before The End',
                            author='Toryiama', 
                            publication_date=2009
                            )
        
    # URL for creating a book
        self.create_book_url = reverse('/books/create/')

    def test_create_book(self):
        '''Ensure we can create book object'''
        data = {
            'title': 'Time', 
            'author': 'Tory', 
            'publication_date': 2010
        }
        response = self.client.post(self.create_book_url, data, format='json')
        # Check that the response status code is 201 (created)
        self.assertEqual(response.data, status.HTTP_201_CREATED)

factory = APIRequestFactory()
create_request = factory.post('/books/create/', {'title': 'Before The End', 'author': 'toryiama', 'publication_date': 2009})
update_request = factory.post('/books/update/', {'title': 'Before The End'})
delete_request = factory.post('/books/delete/', {'author': 'toryiama'})