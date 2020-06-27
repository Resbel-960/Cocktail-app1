from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.

class Tip_c_View(viewsets.ModelViewSet):
    queryset = Tip_category.objects.all()
    serializer_class = Tip_c_Serializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class Tip_View(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = Tip_Serializer
    permission_classes=(IsAuthenticated,)

class Category_View(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class Ingridient_View(viewsets.ModelViewSet):
    queryset = Ingridient.objects.all()
    serializer_class = Ingridient_Serializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

class Cocktail_View(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = Cocktail_Serializer
    # permission_classes=(IsAuthenticatedOrReadOnly,)
    # def post_save(self, *args, **kwargs):
    #     if 'tags' in self.request.DATA:
    #         self.object.tags.set(*self.request.DATA['tags']) # type(self.object.tags) == <taggit.managers._TaggableManager>
    #     return super(Cocktail_View, self).post_save(*args, **kwargs)


class Comment_View(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Comment_Serializer
    # permission_classes=(IsAuthenticatedOrReadOnly,)