from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at', 'comments']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        post = Post.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(post=post, **comment_data)
        return post