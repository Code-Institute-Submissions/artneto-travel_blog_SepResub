from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django import forms
from django.urls import reverse_lazy

# Create your views here.
# Function django views ListView will list the posts from the blog
# DetailView will give the details for the post

def CreateCategoryView(request, caty):
    category_posts =  Post.objects.filter(category=caty)
    return render(request,'category.html', {'caty':caty.title(), 'category_posts':category_posts})


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-publish_date']


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

class CategoryView(CreateView):
    model = Category
    template_name = 'create_category.html'
    fields = '__all__'

class DeleteViewPost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')