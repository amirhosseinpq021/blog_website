from django.urls import path
from . import views

urlpatterns = [

    # path('', views.posts_list, name='posts_list'), # function
    path('', views.PostsListView.as_view(), name='posts_list'),  # class based view

    # path('<int:pk>/', views.post_detail, name='post_detail'),  # function
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # class based view

    # path('add_post/', views.add_post, name='add_post'),  # function
    path('add_post/', views.AddPostView.as_view(), name='add_post'),  # class based view

    # path('edit/<int:pk>/', views.edit_post, name='edit_post'),# function
    path('edit/<int:pk>/', views.EditPostView.as_view(), name='edit_post'),  # class based view

    # path('delete/<int:pk>/', views.delete_post, name='delete_post'),  # function
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),  # class based view

]
