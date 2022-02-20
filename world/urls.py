from django.urls import path
from .views import IndexView, ArticleView, PostView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('article/<int:pk>', ArticleView.as_view(), name='details-article'),
    path('post/', PostView.as_view(), name='post'),
]