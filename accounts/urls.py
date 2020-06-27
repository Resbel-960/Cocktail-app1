from django.urls import path, include
from .views import *
from rest_framework import routers         
from django.conf import settings 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('register/', views.RegisterView.as_view(),  name='register'),
    # path('login/', views.UserLoginAPIView.as_view(),  name='login'),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.jwt')),
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),




]