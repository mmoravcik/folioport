from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib import messages

from folioport.base.mixins import LoginRequiredMixin
from folioport.apps.blog.forms import PostForm

Post = models.get_model('blog', 'Post')
Container = models.get_model('cms', 'Container')
ContainerItems = models.get_model('cms', 'ContainerItems')
Item = models.get_model('cms', 'Item')


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


class ItemCreateRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('folioport:dashboard:cms:item-create',
            kwargs={'class_name': self.request.GET['class_name'],
                    'container_id': self.request.GET['container_id']})


class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/cms/item_create.html'

    def dispatch(self, *args, **kwargs):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return super(ItemCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def form_valid(self, form):
        response = super(ItemCreateView, self).form_valid(form)
        new_item = Item.objects.create(item_class=self.kwargs['class_name'],
            item_id=form.instance.pk)
        container = Container.objects.get(pk=self.kwargs['container_id'])
        ContainerItems.objects.create(container=container,
            item=new_item, position=100)
        messages.info(self.request, 'Item has been created!')
        return response


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'dashboard/cms/item_delete.html'

    def dispatch(self, *args, **kwargs):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return super(ItemDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def delete(self, request, *args, **kwargs):
        Item.objects.filter(
            item_class=self.get_object().__class__.__name__, item_id=self.get_object().pk).delete()
        return super(ItemDeleteView, self).delete(request, *args, **kwargs)


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