from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')



class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_blog')
    category = models.CharField(max_length=255, default='uncategorized')
    body = RichTextField(blank=True, null=True)
    publish_date =  models.DateField(auto_now_add=True)
    article_snippet = models.CharField(max_length=255, default='')


    #This function will display the amount of likes under the posts
    def likes_total(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' - ' + str(self.author)

#This function will redirect my url after submit a post#
    def get_absolute_url(self):
        return reverse('index')
    
