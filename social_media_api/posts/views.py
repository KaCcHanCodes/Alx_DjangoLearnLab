from rest_framework import viewsets, generics, permissions, status
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from  django.contrib.auth import get_user_model
from rest_framework.response import Response
from notifications.models import Notification

# Post views

class ListPost(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    query = Post.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

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
    
    def get_object(self):
        return generics.get_object_or_404(Post, author=self.request.user, pk=self.kwargs['pk'])

class PostFeed(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = self.request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# Comment views

class ListComment(generics.ListAPIView):
    serializer_class = CommentSerializer
    query = Comment.objects.all()
    pagination_class = LimitOffsetPagination

class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

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

# Like views

class LikePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def create(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            Like.objects.get_or_create(user=request.user, post=post)
            Notification.objects.create(receipient=post.author, 
                                        actor=request.user, 
                                        verb = 'Like'
                                        )
            return Response({'message': 'Post liked successfully!'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'message': 'Unable to like post twice!'}, status=status.HTTP_200_OK)

class UnLikePost(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
        except Like.DoesNotExist:
            return Response({'message': "Post Unliked!"}, status=status.HTTP_200_OK)