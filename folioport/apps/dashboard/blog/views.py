from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages

from folioport.base.mixins import FilterUserMixin
from folioport.base.mixins import LoginRequiredMixin
from folioport.apps.blog.forms import PostForm

Post = models.get_model('blog', 'Post')


class PostListView(FilterUserMixin, LoginRequiredMixin, ListView):
    template_name = 'dashboard/blog/list.html'
    model = Post


class PostEditView(FilterUserMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/blog/edit.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:blog:post-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.info(self.request, 'Post has been saved!')
        return super(PostEditView, self).form_valid(form)


class PostCreateView(FilterUserMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/blog/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:blog:post-edit',
            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.info(self.request, 'Post has been created!')
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(FilterUserMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'dashboard/blog/delete.html'

    def get_success_url(self):
        messages.info(self.request, 'Post has been deleted!')
        return reverse_lazy('folioport:dashboard:blog:post-list')