from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

Post = models.get_model('blog', 'Post')
BlogPost = models.get_model('blog', 'BlogPost')


#class PostDetailView(DetailView):
#    template_name = 'pages/blog_post.html'
#    model = Post
#    context_name = 'post'
#
#
#class PostListView(ListView):
#    template_name = 'pages/blog_list.html'
#    model = Post


class PostDetailView(DetailView):
    template_name = 'pages/blog_post.html'
    model = BlogPost


class PostListView(ListView):
    template_name = 'pages/blog_list.html'
    model = BlogPost
