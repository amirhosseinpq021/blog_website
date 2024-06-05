from django.shortcuts import render
from .models import Post

from django.shortcuts import get_object_or_404


# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date_created')
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
