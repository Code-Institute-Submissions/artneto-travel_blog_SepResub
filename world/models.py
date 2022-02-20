from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#here I will define the body content for my blog#



class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' - ' + str(self.author)

#This function will redirect my url after submit a post#
    def get_absolute_url(self):
        return reverse("details-article", args=(str(self.id)))
    
