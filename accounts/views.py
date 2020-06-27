from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from .permisson import IsOwnerProfileOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token



# Create your views here.

class RegisterView(CreateAPIView):
    model = get_user_model()
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = UserRegistrationSerializer

class UserProfileListCreateView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]



