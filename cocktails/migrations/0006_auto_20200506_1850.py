# Generated by Django 3.0.6 on 2020-05-06 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0005_cocktail_ingridient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingridient_cocktail',
            name='cocktail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktails.Cocktail'),
        ),
        migrations.AlterField(
            model_name='ingridient_cocktail',
            name='ingridient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktails.Ingridient'),
        ),
    ]
