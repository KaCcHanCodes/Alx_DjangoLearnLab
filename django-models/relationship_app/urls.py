from django.urls import path
from . import views

urlpatterns = [
    path('list_books', views.book_list, name='list_books'),
    path('library_view', views.library_view.as_view(), name='library_books'),
]