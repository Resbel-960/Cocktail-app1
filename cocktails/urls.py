from django.urls import path, include
from django.conf import settings 
from . import views
from rest_framework import routers         


router = routers.DefaultRouter()
router.register('Tip_categories', views.Tip_c_View)
router.register('Tips', views.Tip_View)
router.register('Ingridients', views.Ingridient_View)
router.register('Category', views.Category_View)
router.register('Cocktails', views.Cocktail_View)
router.register('Comments', views.Comment_View)


urlpatterns = [
    path('', include(router.urls))
]