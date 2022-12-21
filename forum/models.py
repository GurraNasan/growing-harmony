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
