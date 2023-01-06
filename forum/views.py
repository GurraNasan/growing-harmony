from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
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
    model = Post
    category = get_object_or_404(Categories, slug=slug)
    post_form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.category = category
            post = post_form.save()
            return redirect(reverse('forum'))

    template_name = 'add_post.html'
    content = {
        "category": category,
        "post_form": PostForm()

    }
    return render(request, template_name, content)


def DeletePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect(reverse('forum_post'))
    post.delete()
    return redirect(reverse('forum'))