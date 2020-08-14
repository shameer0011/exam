# Generated by Django 3.1 on 2020-08-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_catogery_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catogery',
            name='image',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(max_length=15),
        ),
    ]
