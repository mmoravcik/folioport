from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from folioport.base.mixins import FilterSiteMixin

Post = models.get_model('blog', 'Post')


class PostDetailView(FilterSiteMixin, DetailView):
    template_name = 'pages/blog_post.html'
    model = Post


class PostListView(FilterSiteMixin, ListView):
    template_name = 'pages/blog_list.html'
    model = Post
