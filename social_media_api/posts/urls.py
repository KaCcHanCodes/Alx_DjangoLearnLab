from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Post', views.ListPost, basename='posts')

urlpatterns = [
    path('api/', include(router.urls)),
    path('post/new/', views.CreatePost.as_view()),
    # path('post/list/', views.ListPost.as_view({'get': 'list'})),
    path('post/<int:pk>/update/', views.UpdatePost.as_view()),
    path('post/<int:pk>/delete/', views.DeletePost.as_view()),
    path('post/<int:pk>/comment/new/', views.CreateComment.as_view()),
    path('comment/list/', views.ListComment.as_view()),
    path('comment/<int:pk>/update/', views.UpdateComment.as_view()),
    path('comment/<int:pk>/delete', views.DeleteComment.as_view()),
    path('feed/', views.PostFeed.as_view()),
]