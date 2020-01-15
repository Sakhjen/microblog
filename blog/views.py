from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.


def index(request):
    post_list = Post.objects.filter(date__lte=timezone.now()).order_by('date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(
        request,
        'index.html',
        context={'posts': post_list, 'form': form}
    )