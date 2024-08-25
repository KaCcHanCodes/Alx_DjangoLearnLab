from django.urls import path
import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('list_books', views.list_books, name='list_books'),
    path('LibraryDetailView', views.library_view.as_view(), name='LibraryDetailView'),
    path('UserSignUp', views.register.as_view(), name='UserSignUp'),
    path('login', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view', views.admin_view, name='admin-view'),
    path('librarian-view', views.librarian_view, name='librarian-view'),
    path('member-view', views.member_view, name='member-view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]