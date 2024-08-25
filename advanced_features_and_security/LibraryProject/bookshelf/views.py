from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

def index(request):
    return HttpResponse("Welcome to the library")

@permission_required("bookshelf.can_view", raise_exception=True)
def view(request):
    pass

@permission_required("bookshelf.can_create", raise_exception=True)
def create(request):
    pass

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit(request):
    pass

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete(request):
    pass