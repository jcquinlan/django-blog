from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Blog

def post_list(request):
    posts = Blog.objects.all().order_by('created_date')
    return render(request, 'post_list.html', { "posts": posts })

def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk )
    return render(request, 'post_detail.html', { 'post': post })

def post_new(request):
    return(request, 'post_new.html', {'dog': 'dog!'})
