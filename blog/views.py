from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog_index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_index.html', { 'posts': posts })

def blog_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', { 'post': post })