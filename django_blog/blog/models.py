from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('Edit_Perm', 'Can edit a post'),
            ('Delete_Perm', 'Can delete a post'),
            ('View_Perm', 'Can see posts'),
            ('Create_Perm', 'Can make a post'),
        ]