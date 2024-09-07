from django.urls import include, path
from .views import BookList, BookViewSet
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.authtoken import views

api = SimpleRouter()
api.register(r"Book", BookList)

router = DefaultRouter()
router.register(r'Book', BookViewSet)

urlpatterns = [
    path("api/", include("api.urls")),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)    
]