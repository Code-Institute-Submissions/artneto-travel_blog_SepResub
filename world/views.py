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
    category_posts =  Post.objects.filter(category=caty.replace('-',' '))
    return render(request,'category.html', {'caty':caty.title().replace('-',' '), 'category_posts':category_posts})


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-publish_date']


    def get_context_data(self, *args, **kwargs):
        caty_menu = Category.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["caty_menu"] = caty_menu
        return context

class ArticleView(DetailView):
    model = Post
    template_name = 'details_article.html'

    def get_context_data(self, *args, **kwargs):
        caty_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        context["caty_menu"] = caty_menu
        return context


class PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    
    def get_context_data(self, *args, **kwargs):
        caty_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["caty_menu"] = caty_menu
        return context

class UpdateViewPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_update.html'

class CategoryView(CreateView):
    model = Category
    template_name = 'create_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        caty_menu = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["caty_menu"] = caty_menu
        return context

class DeleteViewPost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')