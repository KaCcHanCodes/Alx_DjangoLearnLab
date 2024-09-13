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
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create-view'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update-view'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete-view'),
    path('tags/<tag_name>/', views.TagsView.as_view()),
    path('search/', views.SearchResultView.as_view()),
]