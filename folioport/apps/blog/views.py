from endless_pagination.views import AjaxListView

from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

Post = models.get_model('blog', 'Post')


class PostDetailView(DetailView):
    template_name = 'pages/blog_post.html'
    model = Post
    queryset = Post.objects.active()


class PostListView(AjaxListView, ListView):
    page_template='pages/partials/list_blog_post.html'
    template_name = 'pages/blog_list.html'
    queryset = Post.objects.active()
    model = Post
