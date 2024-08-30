from django.urls import include, path
# from .views import 
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter
# router.register(r'Book', )

urlpatterns = [
    path("api/", views.BookList.as_view(), name="api.urls"),
]