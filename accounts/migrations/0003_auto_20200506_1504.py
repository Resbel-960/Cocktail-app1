# Generated by Django 3.0.6 on 2020-05-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200506_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
