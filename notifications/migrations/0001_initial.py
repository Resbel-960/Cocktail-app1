# Generated by Django 3.0.6 on 2020-05-24 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_type', models.CharField(choices=[('Greetings', 'G'), ('Info', 'I'), ('NewFollower', 'F'), ('NewLike', 'L'), ('NewComment', 'C'), ('NewFollowerPost', 'P')], max_length=20)),
                ('unseen', models.BooleanField(default=True)),
                ('unread', models.BooleanField(default=True)),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('n_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('n_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]