from django.shortcuts import render, redirect
from blog.models import BlogPost

def not_found(request):
    return render(request, '404.html')

def blog_post_list(request):
    blogs = BlogPost.objects.all()
    return render(request, template_name='blog_list.html', context={'blogs': blogs})


def blog_post_detail(request, pk):
    blog = BlogPost.objects.filter(id=pk).first()
    if not blog:
        return redirect('not_found')
    return render(request, template_name='blog_detail.html', context={'blog': blog})
