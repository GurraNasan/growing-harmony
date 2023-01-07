from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from .models import Categories
from .models import Post
from .forms import PostForm, CommentForm


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
            "forum_category.html",
            {
                "category": category,
                "posts": posts,
                "post_form": PostForm(),
            }
        )


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')

        return render(
            request,
            "forum_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "forum_post.html",
            {
                "post": post,
                "Comments": comments,
                "comment_form": CommentForm,
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


def EditPost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
 
    post_form = PostForm(request.POST or None, request.FILES, instance=post)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.instance.author = request.user
            post = post_form.save()
            return redirect(reverse('forum'))

    template_name = 'edit_post.html'
    content = {
        "post_form": post_form
    }
    return render(request, template_name, content)


def DeletePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(reverse('forum'))