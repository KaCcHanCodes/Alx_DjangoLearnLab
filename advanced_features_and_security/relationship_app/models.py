from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        permissions = (('can_add_book', "Can add books"),
                       ('can_change_book', "can edit book"),
                       ('can_delete_book', 'can delete book')
                    )
        
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLES = [
        ('ADMIN', "Admin"),
        ('LIBRARIAN', "Librarian"),
        ('MEMBER', "Member"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLES, default='MEMBER')

class User_Profile(AbstractUser):
    date_of_birth = models.DateField(input_formats=('%d/%m/%Y'))
    profile_photo = models.ImageField()

    REQUIRED_FIELDS = ["date_of_birth", "profile_photo"]

class UserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo, password = None):
        '''
        Creates and saves user with the following fields.
        '''
        user = self.model(
                        date_of_birth=date_of_birth,
                        profile_photo=profile_photo,
                        )
        user.save(using=self._db)
        return user
    
    def create_superuser(self, date_of_birth, profile_photo):
        '''
        Create superuser with the provided DOB and profile photo
        '''
        user =self.create_user(
                            date_of_birth=date_of_birth,
                            profile_photo=profile_photo,
                            )
        user.is_admin = True
        user.save(using=self._db)
        return user