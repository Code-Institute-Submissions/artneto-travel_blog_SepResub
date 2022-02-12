from django.contrib import admin
from .models import Post

#this function allows the post entries to be accessible from the main area
admin.site.register(Post)
