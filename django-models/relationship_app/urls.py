from django.urls import path
import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('list_books', views.list_books, name='list_books'),
    path('LibraryDetailView', views.library_view.as_view(), name='LibraryDetailView'),
    path('UserSignUp', views.UserRegistration.as_view(), name='UserSignUp'),
    path('login', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='relationship_app/logout.html', name='logout')),
]