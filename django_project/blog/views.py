from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mary Jane',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 12, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 19, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
