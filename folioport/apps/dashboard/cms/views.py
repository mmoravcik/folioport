from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages

from folioport.base.mixins import LoginRequiredMixin
from folioport.apps.blog.forms import PostForm

Post = models.get_model('blog', 'Post')
Container = models.get_model('cms', 'Container')


class ContainerListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/cms/container_list.html'
    model = Container


class ContainerEditView(LoginRequiredMixin, UpdateView):
    model = Container
    template_name = 'dashboard/cms/edit.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def form_valid(self, form):
        messages.info(self.request, 'Post has been saved!')
        return super(ContainerEditView, self).form_valid(form)


class ItemEditView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/cms/item_edit.html'

    def get_queryset(self):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return self.model.objects.filter(id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def form_valid(self, form):
        messages.info(self.request, 'Item has been saved!')
        return super(ItemEditView, self).form_valid(form)


class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/cms/item_create.html'

    def get_queryset(self):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return self.model.objects.filter(id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def form_valid(self, form):
        messages.info(self.request, 'Item has been created!')
        return super(ItemCreateView, self).form_valid(form)



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/blog/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:blog:post-list')

    def form_valid(self, form):
        messages.info(self.request, 'Post has been created!')
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'dashboard/blog/delete.html'

    def get_success_url(self):
        messages.info(self.request, 'Post has been deleted!')
        return reverse_lazy('folioport:dashboard:blog:post-list')