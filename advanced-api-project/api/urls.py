from django.urls import path
from . import views

urlpattterns = [
    path('/books/', views.BookListView.as_view()),
    path('/books/<int:pk>/', views.BookDetailView.as_view()),
    path('/books/create/', views.BookCreateView.as_view()),
    path('/books/update/', views.BookUpdateView.as_view()),
    path('/books/delete/', views.BookDeleteView.as_view()),
]