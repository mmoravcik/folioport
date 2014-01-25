from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages

from folioport.apps.blog.forms import PostForm

Post = models.get_model('blog', 'Post')


class PostDetailView(DetailView):
    template_name = 'pages/blog_post.html'
    model = Post
    context_name = 'post'


class PostListView(ListView):
    template_name = 'dashboard/blog/list.html'
    model = Post


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/blog/edit.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:blog:post-list')

    def form_valid(self, form):
        messages.info(self.request, 'Post has been saved!')
        return super(PostEditView, self).form_valid(form)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/blog/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:blog:post-list')

    def form_valid(self, form):
        messages.info(self.request, 'Post has been created!')
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('folioport:dashboard:blog:post-list')
    template_name = 'dashboard/blog/delete.html'

    def form_valid(self, form):
        messages.info(self.request, 'Post has been deleted!')
        return super(PostCreateView, self).form_valid(form)
