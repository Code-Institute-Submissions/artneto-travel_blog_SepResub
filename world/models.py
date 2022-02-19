from django.db import models
from django.contrib.auth.models import User

'''here I will define the body content for my blog'''


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Hello world Blog!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' - ' + str(self.author)
