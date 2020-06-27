from django.db import models
from django.conf import settings 



# Create your models here.

class Notification(models.Model):

    TYPE_CHOICES = (
        ('Greetings', 'Greetings'),
        ('Info', 'Info'),
        ('NewFollower', 'NewFollower'),
        ('NewLike', 'NewLike'),
        ('NewComment', 'NewComment'),
        ('NewFollowerPost', 'NewFollowerPost'),
        ('NewFollowerTip', 'NewFollowerTip')
    )
    n_sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notification_sender', on_delete=models.CASCADE)
    n_receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notification_receiver',  on_delete=models.CASCADE)
    n_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    unseen = models.BooleanField(default=True)
    unread = models.BooleanField(default=True)
    send_date = models.DateTimeField( auto_now_add=True)
    body= models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.n_type} --  {self.send_date}'