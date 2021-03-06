# Generated by Django 3.0.6 on 2020-05-24 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0008_auto_20200519_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cocktail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cocktails.Cocktail'),
        ),
        migrations.AlterField(
            model_name='like',
            name='cocktail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='cocktails.Cocktail'),
        ),
    ]
