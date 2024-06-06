from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm
from django.shortcuts import get_object_or_404


# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date_created').filter(status='pub')
    context = {
        'posts_list': posts,
    }
    return render(request, 'blog/posts_list.html', context)


def post_detail(request, pk):
    post_details = get_object_or_404(Post, pk=pk)
    context = {
        'post_details': post_details,
    }
    return render(request, 'blog/post_detail.html', context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = AddPostForm()

    context = {
        'form': form,
    }
    return render(request, 'blog/add_post.html', context)














