from django.urls import path
from . import views

urlpattterns = [
    path('/books/', views.BookListView.as_view()),
    path('/books/<int:pk>/', views.BookDetailView.as_view()),
    path('/create_books/', views.BookCreateView.as_view()),
    path('/update_books/', views.BookUpdateView.as_view()),
    path('delete_books', views.BookDeleteView.as_view()),
]