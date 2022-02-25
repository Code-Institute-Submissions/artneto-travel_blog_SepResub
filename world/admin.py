from django.contrib import admin
from .models import Post, Category

#this function allows the post entries to be accessible from the main area
admin.site.register(Post)
admin.site.register(Category)
