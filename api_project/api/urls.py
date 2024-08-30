from django.urls import include, path
from .views import BookList
from . import views
from rest_framework.routers import SimpleRouter

api = SimpleRouter()
api.register(r"Book", BookList)

urlpatterns = [
    path("api/", include("api.urls")),
]