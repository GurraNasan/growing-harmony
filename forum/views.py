from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Categories
from .models import Post


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


class CategoryList(generic.ListView):
    model = Categories
    template_name = 'forum.html'
    queryset = Categories.objects.all()


class CategoryDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Categories.objects
        category = get_object_or_404(queryset, slug=slug)
        posts = category.post_category.order_by('created_on')
        
        return render(
            request,
            "forum_post.html",
            {
                "category": category,
                "posts": posts
            }
        )
    


