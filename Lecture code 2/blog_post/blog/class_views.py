from django.views.generic import ListView, DetailView
from blog.models import BlogPost

class BlogPostyListView(ListView):
    model = BlogPost
    template_name = 'class_blog_list.html'
    context_object_name = 'blogs'
    queryset = BlogPost.objects.filter(deleted=False).order_by('-id')

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'class_blog_detail.html'
    context_object_name = 'blog'