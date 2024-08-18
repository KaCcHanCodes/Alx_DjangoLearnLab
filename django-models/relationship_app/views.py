from django.shortcuts import render
from models import Book

def book_list(request):
    '''This view should render a simple text list of book titles and their authors.'''
    book = Book.objects.all()
    context = {'book_list': book}
    return render(request, 'book/book_list.html', context)
