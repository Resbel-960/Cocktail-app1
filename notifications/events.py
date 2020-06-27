from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import threading
from django.conf import settings 
from accounts.models import User, Follower
from cocktails.models import *

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t






