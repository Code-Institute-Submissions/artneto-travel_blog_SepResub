from django.contrib import admin
from .models import Post, Category, Profile

#This function allows the post entries to be accessible from the main area
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)