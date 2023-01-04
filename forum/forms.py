from .models import Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'featured_image',
        )
        widgets = {
            'content': SummernoteWidget(),
        }
