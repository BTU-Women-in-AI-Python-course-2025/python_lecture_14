from django import forms
from blog.models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    banner_image = forms.ImageField(label="Banner image", required=False)

    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'active', 'document', 'category', 'authors', 'banner_image']
