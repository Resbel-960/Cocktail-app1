from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Model
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# user delete olunsa followerler nece olsun?
# Create your models here.

class User(AbstractUser):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    USER_CHOICES = (
        ('1', 'Basic'),
        ('2', 'Barmen'),
        ('3', 'Barista'),
    )
    
    birthdate = models.DateField( auto_now=False, auto_now_add=False, null=True)
    phone= models.CharField(max_length=15, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateTimeField( auto_now_add=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES)
    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['email', 'user_type']


class Follower(models.Model):

    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.follower} --- {self.following}'
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


@receiver (post_save, sender = settings.AUTH_USER_MODEL)
def  create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

