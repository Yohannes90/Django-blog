from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CategoryCreateView,
    CategoryPostListView,
    CategoryListView,
    CategoryUpdateView,
    CategoryDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<str:category>', CategoryPostListView.as_view(), name='category-posts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('categories/<str:category>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('about/', views.about, name='blog-about'),
    path('post/<str:category>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('like/<int:pk>/', views.LikeView, name='like-post'),
]
