from django.contrib import admin
from .models import Categories
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['title']

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'content'

    list_filter = ['title', 'created_on']
    search_fields = ['title', 'created_on']
    list_display = ['title', 'created_on']