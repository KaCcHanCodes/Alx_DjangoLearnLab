from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.customlogin, name='login'),
    path('logout/', views.customlogout, name='logout'),
]