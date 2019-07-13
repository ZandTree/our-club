from django.shortcuts import render,reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class Home(TemplateView):
    """
    auth user gets redirected to all posts
    """
    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("posts:all"))
        return super().get(request,*args,**kwargs)
