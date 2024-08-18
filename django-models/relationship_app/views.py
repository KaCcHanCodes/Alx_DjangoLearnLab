from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

def list_books(request):
    '''This view should render a simple text list of book titles and their authors.'''
    book = Book.objects.all()
    context = {'book_list': book}
    return render(request, 'relationship_app/list_books.html', context)

class library_view(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library

class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy(login)
    template_name = 'relationship_app/register.html'

@user_passes_test
def admin_view(request):
    return render(request, 'relationship_app/admin-view')

@user_passes_test
def librarian_view(request):
    return render(request, 'relationship_app/librarian-view')

@user_passes_test
def member_view(request):
    return render(request, 'relationship_app/member-view')