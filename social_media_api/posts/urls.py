from django.urls import path
from . import views

urlpatterns = [
    path('post/new/', views.CreatePost.as_view()),
    path('post/list/', views.ListPost.as_view({'get': 'list'})),
    path('post/<int:pk>/update/', views.UpdatePost.as_view()),
    path('post/<int:pk>/delete/', views.DeletePost.as_view()),
    path('post/<int:pk>/comment/new/', views.CreateComment.as_view()),
    path('comment/list/', views.ListComment.as_view()),
    path('comment/<int:pk>/update/', views.UpdateComment.as_view()),
    path('comment/<int:pk>/delete', views.DeleteComment.as_view()),
    path('feed/', views.PostFeed.as_view()),
]