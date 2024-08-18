from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def list_books(request):
    '''This view should render a simple text list of book titles and their authors.'''
    book = Book.objects.all()
    context = {'book_list': book}
    return render(request, 'relationship_app/list_books.html', context)

class library_view(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library