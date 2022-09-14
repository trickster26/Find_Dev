from django.urls import path
from . import views


urlpatterns = [
    path('',views.profiless, name="profiless"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile")
]
