from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Categories(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    categorie_image = CloudinaryField('image', default='placeholder')

    class Meta:
        # Arrange the categories after title
        ordering = ['title']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='post_category')

    class Meta:
        # Arrange the post by when they are created
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    # code is copied from I think there for i blog, Code Institute

    post = models.ForeignKey(Post, on_delete=models.CASCADE,  related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        # Arrange the comments in Ascending order.

        ordering = ['created_on']

        def __str__(self):
            return f"Comment {self.comment} by {self.name}"
