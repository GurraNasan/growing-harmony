from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Categories
from .models import Post
from .forms import PostForm


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
                "posts": posts,
                "post_form": PostForm()
            }
        )


def AddPost(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    post_form = PostForm(request.POST)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.category = category
            post = post_form.save()
            return redirect(request,'forum_post.html')

    template_name = 'add_post.html'
    content = {
        "category": category,
        "post_form": PostForm()
                
    }
    return render(request, template_name, content)