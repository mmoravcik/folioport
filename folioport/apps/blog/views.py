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
        ctx = super(PostDetailView, self).get_context_data()
        ctx['next_post'] = self.get_object().next()
        ctx['previous_post'] = self.get_object().previous()
        ctx['blog_active'] = True
        return ctx


class PostPreview(PostDetailView):
    template_name = 'pages/preview.html'
    context_name = 'object'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostListView(AjaxListView, ListView):
    page_template='pages/partials/list_blog_post.html'
    template_name = 'pages/blog_list.html'
    queryset = Post.site_objects.active()
    model = Post

    def get_context_data(self, **kwargs):
        ctx = super(PostListView, self).get_context_data(**kwargs)
        ctx['blog_active'] = True
        return ctx
