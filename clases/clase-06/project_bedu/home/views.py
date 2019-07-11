from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class HomeView(View):
    """docstring for HomeView."""
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request,'home.html',locals())
    # def __init__(self, arg):
    #     super(HomeView, self).__init__()
    #     self.arg = arg

class PostView(View):
    @property
    def pk(self, *args, **kwargs):
        return self.kwargs['pk']

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.pk)
        return render(request,'post.html',locals())
