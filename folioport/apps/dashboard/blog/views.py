from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.sites.models import get_current_site

from folioport.base.mixins import FilterUserMixin
from folioport.base.mixins import LoginRequiredMixin, AjaxableResponseMixin
from folioport.apps.blog.forms import PostForm

Post = models.get_model('blog', 'Post')


class PostListView(FilterUserMixin, LoginRequiredMixin, ListView):
    template_name = 'dashboard/blog/list.html'
    model = Post


class PostEditView(FilterUserMixin, LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/blog/edit.html'

    def get_success_url(self):
        messages.success(self.request, 'Post has been saved!')
        return reverse_lazy('folioport:dashboard:blog:post-edit',
                            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super(PostEditView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(PostEditView, self).get_context_data(**kwargs)
        if self.request.POST and not kwargs['form'].is_valid():
            ctx['active_tab'] = 'settings-tab'
        return ctx

class PostCreateView(FilterUserMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/blog/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:blog:post-edit',
            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.site = get_current_site(self.request)
        form.instance.user = self.request.user
        messages.info(self.request, 'Post has been created!')
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(FilterUserMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'dashboard/blog/delete.html'

    def get_success_url(self):
        messages.info(self.request, 'Post has been deleted!')
        return reverse_lazy('folioport:dashboard:blog:post-list')