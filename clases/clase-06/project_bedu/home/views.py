from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    """docstring for HomeView."""
    def get(self, request, *args, **kwargs):
        return render(request,'home.html',locals())
    # def __init__(self, arg):
    #     super(HomeView, self).__init__()
    #     self.arg = arg
