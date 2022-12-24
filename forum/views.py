from django.shortcuts import render
from django.views import generic
from .models import Categories
from .models import Post


class CategoriesList(generic.ListView):
    model = Categories
    template_name = 'index.html'
    paginate_by = 8
