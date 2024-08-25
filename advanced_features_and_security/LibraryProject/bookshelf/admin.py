from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")
admin.site.register(Book, BookAdmin)

class ModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": 
                                               ["date_of_birth", "profile_photo"]}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields": 
                                                   ["date_of_birth", "profile_photo"]}),)
    
    admin.site.register(CustomUser, UserAdmin)