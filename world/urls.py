"""Libraries"""
from django.urls import path
from .views import IndexView, ArticleView, PostView, UpdateViewPost,\
     DeleteViewPost, CategoryView, CreateCategoryView, LikeView,\
     AddCommentView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('article/<int:pk>', ArticleView.as_view(), name='details_article'),
    path('post/', PostView.as_view(), name='post'),
    path('create_category/', CategoryView.as_view(), name='create_category'),
    path('article/edit/<int:pk>', UpdateViewPost.as_view(),
         name='update_post'),
    path('article/<int:pk>/delete', DeleteViewPost.as_view(),
         name='post_delete'),
    path('category/<str:caty>/', CreateCategoryView, name='category'),
    path('like/<int:pk>/', LikeView, name='post_like'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(),
         name='add_your_comments'),
]
