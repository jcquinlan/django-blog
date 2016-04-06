from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Blog
from .forms import BlogForm

def post_list(request):
    posts = Blog.objects.all().order_by('created_date')
    return render(request, 'post_list.html', { "posts": posts })

def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk )
    return render(request, 'post_detail.html', { 'post': post })

def post_new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            # this line adds the title and text to the post, since we specified in
            # models.py to create the form with the title and text inputs
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogForm()

    return render(request, 'post_new.html', {'form': form })
