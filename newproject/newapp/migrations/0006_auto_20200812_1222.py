# Generated by Django 3.1 on 2020-08-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_auto_20200812_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='image1',
            field=models.ImageField(default='image.jpg', upload_to='image2'),
        ),
        migrations.AlterField(
            model_name='catogery',
            name='image',
            field=models.ImageField(default='image.jpg', upload_to='image'),
        ),
    ]
