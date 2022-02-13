from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# Function django views ListView will list the posts from the blog
# DetailView will give the details for the post

class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'details_article.html'
