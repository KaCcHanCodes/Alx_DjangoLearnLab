from django.urls import include, path
from .views import BookList, BookViewSet
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

route = SimpleRouter()
route.register(r"api.urls", BookList)

router = DefaultRouter()
router.register(r'Book', BookViewSet)

urlpatterns = [
    path("api/", include(route.urls)),
    path('', include(router.urls)),
]