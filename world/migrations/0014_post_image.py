# Generated by Django 3.2 on 2022-04-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder', upload_to='images/'),
        ),
    ]