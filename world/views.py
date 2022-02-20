from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm
from django import forms

# Create your views here.
# Function django views ListView will list the posts from the blog
# DetailView will give the details for the post

class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'details_article.html'


class PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    

class UpdateViewPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_update.html'
    #fields = ['title', 'title_tag', 'body']