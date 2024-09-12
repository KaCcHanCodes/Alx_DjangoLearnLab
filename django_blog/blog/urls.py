from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('/posts/', views.posts.as_view(), name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.customlogin, name='login'),
    path('logout/', views.customlogout, name='logout'),
    path('/posts/new/', views.postcreate.as_view(), name='create-view'),
    path('/posts/<int:pk>/',views.postdetail.as_view(), name='detail-view'),
    path('/posts/<int:pk>/edit/', views.postupdate.as_view(), name='update-view'),
    path('/posts/<int:pk>/delete/', views.postdelete.as_view(), name='delete-view'),
]