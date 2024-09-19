from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

# Post views

class ListPost(generics.ListAPIView):
    serializer_class = PostSerializer
    query = Post.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(settings.AUTH_USER_MODEL, id=self.request.data.get('author'))
        return serializer.save(author=author)
    
class UpdatePost(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# Comment views

class ListComment(generics.ListAPIView):
    serializer_class = CommentSerializer
    query = Comment.objects.all()
    pagination_class = LimitOffsetPagination

class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(settings.AUTH_USER_MODEL, id=self.request.data.get('author'))
        return serializer.save(author=author)
   
class UpdateComment(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class DeleteComment(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()