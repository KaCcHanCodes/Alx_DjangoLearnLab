from django.urls import include, path
from .views import BookList, BookViewSet
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

api = SimpleRouter()
api.register(r"Book", BookList)

router = DefaultRouter()
router.register(r'Book', BookViewSet)

urlpatterns = [
    path("api/", include("api.urls")),
    path('', include(router.urls)),
]