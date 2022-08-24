""" Libraries View """
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,\
     CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django import forms
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# Function django views ListView will list the posts from the blog
# DetailView will give the details for the post


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('details_article', args=[str(pk)]))


def CreateCategoryView(request, caty):
    category_posts = Post.objects.filter(category=caty.replace('-', ' '))
    return render(request, 'category.html', {
                           'caty': caty.title().replace('-', ' '),
                           'category_posts': category_posts})


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-publish_date']
    caty = Category.objects.all()
    paginate_by = 3

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

        content = get_object_or_404(Post, id=self.kwargs['pk'])
        likes_total = content.likes_total()

        liked = False
        if content.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["likes_total"] = likes_total
        context["caty_menu"] = caty_menu
        context["liked"] = liked
        return context


class PostView(CreateView):
    model = Post
    template_name = 'post.html'
    form_class = PostForm

    def get_context_data(self, *args, **kwargs):
        caty_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["caty_menu"] = caty_menu
        return context


class AddCommentView(CreateView):
    
    model = Comment
    form_class = CommentForm
    template_name = 'comments_box.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


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
