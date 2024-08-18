from django.urls import path
import views
from .views import list_books

urlpatterns = [
    path('list_books', views.list_books, name='list_books'),
    path('LibraryDetailView', views.library_view.as_view(), name='LibraryDetailView'),
]