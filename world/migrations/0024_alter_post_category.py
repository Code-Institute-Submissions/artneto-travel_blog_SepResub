# Generated by Django 3.2 on 2022-09-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0023_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='category', max_length=255),
        ),
    ]