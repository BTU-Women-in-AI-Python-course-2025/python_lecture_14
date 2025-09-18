from django.urls import path
from blog.views import (
    not_found,
    blog_post_list,
    blog_post_detail,
    blog_create,
    blog_update,
    blog_delete
)

urlpatterns = [
    path('not_found', not_found, name='not_found'),
    path('blog_list/', blog_post_list, name='blog_list'),
    path('blog_detail/<int:pk>/', blog_post_detail, name='blog_detail'),
    path('blog_create/', blog_create, name='blog_create'),
    path('blog_update/<int:pk>/', blog_update, name='blog_update'),
    path('blog_delete/<int:pk>/', blog_delete, name='blog_delete'),
]
