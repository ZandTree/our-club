from django.shortcuts import render
from django.views.generic import ListView,DeleteView,DetailView
from .models import Post

class PostList(ListView):
    model = Post


# to do:
#AllPosts,CreatePostm,
#UserPosts,SinglePost,
#DeletePost
