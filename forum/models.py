from django.db import models
from django.conf.auth.models import User
from cloudinary.models import CloudinaryField


class Categories(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    categorie_image = CloudinaryField('image', default='placeholder')

    class Meta:
        # Arrange the categories after title
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    categorie_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    exerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        # Arrange the post by when they are created  
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)