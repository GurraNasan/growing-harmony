from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from .models import Categories
from .models import Post


class CategoriesList(generic.ListView):
    model = Categories
    template_name = 'forum.html'
    paginate_by = 8


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')