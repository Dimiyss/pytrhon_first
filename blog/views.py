from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/base.html', {'posts': posts})

def post_detail(request,pk):
    posts = (get_object_or_404(Post, pk=pk),)
    return render(request, 'blog/base.html', {'posts': posts})