# Generated by Django 3.0.6 on 2020-07-15 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0009_auto_20200524_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reply_set', to='cocktails.Comment'),
        ),
    ]
