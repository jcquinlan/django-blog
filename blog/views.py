from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

def post_list(request):
    posts = Blog.objects.all().order_by('created_date')
    return render(request, 'post_list.html', { "posts": posts })
