from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('posts/', views.posts.as_view(), name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.customlogin, name='login'),
    path('logout/', views.customlogout, name='logout'),
    path('post/new/', views.postcreate.as_view(), name='create-view'),
    path('posts/<int:pk>/',views.postdetail.as_view(), name='detail-view'),
    path('post/<int:pk>/update/', views.postupdate.as_view(), name='update-view'),
    path('post/<int:pk>/delete/', views.postdelete.as_view(), name='delete-view'),
    path('post/<int:post_id>/comments/new/', views.commentcreate.as_view(), name='comment-create-view'),
    path('post/<int:pk>/comment-update/', views.commentupdate.as_view(), name='comment-update-view'),
    path('post/<int:pk>/comment-delete/', views.commentdelete.as_view(), name='comment-delete-view'),
]