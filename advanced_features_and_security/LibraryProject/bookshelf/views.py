from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

def index(request):
    return HttpResponse("Welcome to the library")

@permission_required("bookshelf.can_view", raise_exception=True)
def view(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, context)


@permission_required("bookshelf.can_create", raise_exception=True)
def create(request):
    pass

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit(request):
    pass

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete(request):
    pass

def get_title(request):
    # if request is a POST request process form data.
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form is valid")
        
    # if a GET (or other methods) direct to register
    else:
        form = ExampleForm()
        return render(request, "register.html")