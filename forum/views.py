from django.shortcuts import render
from django.views import generic, View
from .models import Categories
from .models import Post


def home(request):
    return render(request, 'index.html')


class CategoryList(generic.ListView):
    model = Categories
    template_name = 'forum.html'
    queryset = Categories.objects.all()


# class PostList(generic.ListView):
#    model = Post
#    queryset = Post.objects.order_by('-created_on')
#    template_name = 'forum.html'

def contact(request):
    return render(request, 'contact.html')
