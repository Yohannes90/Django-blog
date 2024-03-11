from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Category


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # post = get_object_or_404(Post, id=self.kwargs['title'])
        context['categories'] = Category.objects.all()
        # context['total_likes'] = post.total_likes()
        # context['pk'] = post.pk
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'content']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['category']
    success_url = '/category'


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, category=self.kwargs.get('category'))
        return Post.objects.filter(category=category).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/categories.html'
    context_object_name = 'categories'
    paginate_by = 5


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['category']


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = '/category'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'content']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-home'))
