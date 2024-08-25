from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_Profile
# Register your models here.

class ModelAdmin(UserAdmin):
    # admin.site.register(User_Profile, UserAdmin)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": 
                                               ["date_of_birth", "profile_photo"]}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields": 
                                                   ["date_of_birth", "profile_photo"]}),)