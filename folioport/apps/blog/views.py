from endless_pagination.views import AjaxListView

from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

Post = models.get_model('blog', 'Post')


class PostDetailView(DetailView):
    template_name = 'pages/blog_post.html'
    model = Post
    queryset = Post.site_objects.active()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context['next_post'] = self.get_object().next()
        context['previous_post'] = self.get_object().previous()
        return context


class PostListView(AjaxListView, ListView):
    page_template='pages/partials/list_blog_post.html'
    template_name = 'pages/blog_list.html'
    queryset = Post.site_objects.active()
    model = Post
