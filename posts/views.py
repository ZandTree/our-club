from django.shortcuts import render
from django.views.generic import View

class PostList(View):
    def get(self,request):
        print("where is my page")
        return render(request,'posts/post_list.html')

def index(request):
    return render(request,'index.html')
