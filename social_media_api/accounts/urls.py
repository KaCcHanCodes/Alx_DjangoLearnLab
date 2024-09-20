from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('profile/', views.ProfileUpdateView.as_view()),
    path('follow/<int:user_id>/', views.FollowView.as_view()),
    path('unfollow/<int:user_id>/', views.UnfollowView.as_view()),
]