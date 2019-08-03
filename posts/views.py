from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DeleteView,DetailView,CreateView
from .models import Post
from .forms import PostForm
from django.http import Http404
from django.contrib.auth.models import User
from braces.views import PrefetchRelatedMixin,SetHeadlineMixin,SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class AllPosts(ListView):
    model = Post

class UserPost(ListView):
    model = Post
    template_name = 'posts/user_timeline.html'

    def get_queryset(self,**kwargs):
        try:
            """finding particular user"""
            name = self.kwargs.get('member')
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=name)

        except User.DoesNotExist:
            return Http404
        else:
            """ if try OK, you get access to else;
            from object post to its attr user (self.post_user)
            """
            qs = self.post_user.posts.all()
        return qs
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['post_user'] = self.post_user
        context['timeline'] = True
        return  context


class SinglePost(SelectRelatedMixin, DetailView):
    model = Post
    select_related = ("user", "community")

    def get_queryset(self,**kwargs):
        """ limit queryset by only post of a particular user"""
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )
    def get_object(self):
        """ get 'username' from url kwargs"""
        name = self.kwargs.get('username',None)
        return  get_object_or_404(Post,user__username__iexact = name )



class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
