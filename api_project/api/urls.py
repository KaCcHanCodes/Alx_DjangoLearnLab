from django.urls import include, path
# from .views import 
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter
# router.register(r'Book', )

urlpatterns = [
    path("api.urls", views.BookList.as_view(), name="BookList"),
]