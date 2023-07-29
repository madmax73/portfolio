from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.

def blog(request):
    return render(request, 'blog/blog.html')

def single(request):
    return render(request, 'blog/single.html')
