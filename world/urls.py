from django.urls import path
from .views import IndexView, ArticleView, PostView, UpdateViewPost

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('article/<int:pk>', ArticleView.as_view(), name='details-article'),
    path('post/', PostView.as_view(), name='post'),
    path('article/edit/<int:pk>', UpdateViewPost.as_view(), name='update_post')
]