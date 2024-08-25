from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField

class CustomUser(AbstractUser):
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