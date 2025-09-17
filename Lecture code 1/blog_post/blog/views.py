from django.shortcuts import render, redirect

from blog.forms import BlogPostModelForm
from blog.models import BlogPost, BannerImage


def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, template_name='blog_list.html', context={'blog_posts': blog_posts})


def blog_post_detail(request, pk):
    blog = BlogPost.objects.filter(pk=pk).first()
    if not blog:
        return redirect('not_found')
    return render(request, template_name='blog_detail.html', context={'blog': blog})

def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            banner_image = form.cleaned_data['banner_image']
            BannerImage.objects.create(blog_post=blog_post, image=banner_image)
            return redirect('blog_post_list')
    else:
        form = BlogPostModelForm()
    return render(request, template_name='blog_create.html', context={'form': form})


def not_found(request):
    return render(request, template_name='404.html')
