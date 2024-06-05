from django.shortcuts import render
from .models import Post


# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date_created')
    context = {
        'posts_list': posts,
    }
    return render(request, 'blog/posts_list.html', context)
