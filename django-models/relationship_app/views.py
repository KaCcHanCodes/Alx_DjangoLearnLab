from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView

def book_list(request):
    '''This view should render a simple text list of book titles and their authors.'''
    book = Book.objects.all()
    context = {'book_list': book}
    return render(request, 'relationship_app/list_books.html', context)

class library_view(ListView):
    template_name = 'relationship_app/library_detail.html'
    queryset = Library.objects.all()