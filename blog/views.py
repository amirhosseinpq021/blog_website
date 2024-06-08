from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm, EditPostForm
from django.shortcuts import get_object_or_404

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# _________________________________________________________________________________________________________________

# def posts_list(request):
#     posts = Post.objects.all().order_by('-date_created').filter(status='pub')
#     context = {
#         'posts_list': posts,
#     }
#     return render(request, 'blog/posts_list.html', context)


class PostsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):  # override this method
        return Post.objects.all().order_by('-date_created').filter(status='pub')



# _________________________________________________________________________________________________________________
# def post_detail(request, pk):
#     post_details = get_object_or_404(Post, pk=pk)
#     context = {
#         'post_details': post_details,
#     }
#     return render(request, 'blog/post_detail.html', context)


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_details'


# _________________________________________________________________________________________________________________
# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'blog/add_post.html', context)


class AddPostView(LoginRequiredMixin, generic.CreateView):
    form_class = AddPostForm
    template_name = 'blog/add_post.html'
    context_object_name = 'form'


    def form_valid(self, form):  # new
        form.instance.author = self.request.user
        return super().form_valid(form)


# _________________________________________________________________________________________________________________
# def edit_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = EditPostForm(request.POST or None, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = EditPostForm(instance=post)
#     context = {
#         'form': form,
#     }
#     return render(request, 'blog/add_post.html', context)


class EditPostView(generic.UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/add_post.html'
    context_object_name = 'form'


# _________________________________________________________________________________________________________________
# def delete_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('posts_list')


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts_list')


# _________________________________________________________________________________________________________________
def search_posts(request):
    keyword = request.GET.get('keyword')

    blog_search = Post.objects.filter(
        Q(title__icontains=keyword) | Q(text__icontains=keyword) | Q(author__username__icontains=keyword) |
        Q(status__icontains=keyword))

    context = {
        'blogs': blog_search,
        'keyword': keyword,
    }
    return render(request, 'blog/search.html', context)
# _________________________________________________________________________________________________________________

