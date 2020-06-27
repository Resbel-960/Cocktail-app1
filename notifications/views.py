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
from notifications.models import *

# post save trigger

def notification_test_page(request):
    return render(request, 'index.html')

@receiver(post_save, sender=User)
def new_user(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        admin=User.objects.get(id=1)
        data = "Welcome " + str(instance.username) +'. Thank you for joining us!'
        async_to_sync(channel_layer.group_send)(
            str(instance.id),
            {
                'type':'notify',
                'content':data,
            }
        )
        Notification.objects.create(n_sender=admin, n_receiver=instance, n_type='Greetings', body=data)


@receiver(post_save, sender=Cocktail)
def new_cocktail(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data = 'Hey, ' + str(instance.author) + " posted a new Cocktail!"
        id_num = instance.author.id
        user= User.objects.get(id=id_num)

        if Follower.objects.filter(following =user):
            followers=Follower.objects.filter(following =user)
            for e in followers:
                async_to_sync(channel_layer.group_send)(
                str(e.follower.id),
                {
                    'type':'notify',
                    'content':data,
                }
                )
                Notification.objects.create(n_sender=instance.author, n_receiver=e.follower, n_type='NewFollowerPost', body=data)



@receiver(post_save, sender=Tip)
def new_tip(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data = 'Hey, ' + str(instance.author) + " posted a new Tip!"
        id_num = instance.author.id
        user= User.objects.get(id=id_num)

        if Follower.objects.filter(following =user):
            followers=Follower.objects.filter(following =user)
            for e in followers:
                async_to_sync(channel_layer.group_send)(
                str(e.follower.id),
                {
                    'type':'notify',
                    'content':data,
                }
                )
                Notification.objects.create(n_sender=instance.author, n_receiver=e.follower, n_type='NewFollowerTip', body=data)


@receiver(post_save, sender=Comment)
def new_comment(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data = 'Hey, ' + str(instance.author) + " commented on your Cocktail!"
        cocktail_autor= instance.cocktail.author
        print(cocktail_autor)
        async_to_sync(channel_layer.group_send)(
            str(cocktail_autor.id),
            {
                'type':'notify',
                'content':data,
            }
        )
        Notification.objects.create(n_sender=instance.author, n_receiver=instance.cocktail.author, n_type='NewComment', body=data)



@receiver(post_save, sender=Follower)
def new_follower(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data = 'Hey, ' + str(instance.follower) + " followed you!"
        following=instance.following
        async_to_sync(channel_layer.group_send)(
            str(following.id),
            {
                'type':'notify',
                'content':data,
            }
        )
        Notification.objects.create(n_sender=instance.follower, n_receiver=instance.following, n_type='NewFollower', body=data)



@receiver(post_save, sender=Like)
def new_like(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data = 'Hey, ' + str(instance.user) + " liked your Cocktail!"
        cocktail_author= instance.cocktail.author
        async_to_sync(channel_layer.group_send)(
            str(cocktail_author.id),
            {
                'type':'notify',
                'content':data,
            }
        )
        Notification.objects.create(n_sender=instance.user, n_receiver=instance.cocktail.author, n_type='NewLike', body=data)


def info():
    channel_layer = get_channel_layer()
    data= 'Dear Users, it is just an info notification'
    users=User.objects.all()
    admin= User.objects.get(id=1)
    for e in users:
        async_to_sync(channel_layer.group_send)(
            str(e.id),
            {
                'type':'notify',
                'content':data,
            }
        )
        Notification.objects.create(n_sender=admin, n_receiver=e, n_type='Greetings', body=data)

# # set_interval(info, 5)

def show_unseen_notification(request):
    unseen_n= Notification.objects.filter(n_receiver=request.user, unseen=True)
    for msj in unseen_n:
        print(msj.body)