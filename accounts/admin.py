from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)


class FollowerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Follower, FollowerAdmin)