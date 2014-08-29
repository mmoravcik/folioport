from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib import messages

from folioport.base.mixins import LoginRequiredMixin

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

    def get_form_class(self):
        if self.model.get_form_class():
            return self.model.get_form_class()
        return super(ItemEditView, self).get_form_class()

    def get_template_names(self):
        if self.model.get_edit_create_template():
            return [self.model.get_edit_create_template()]
        return [self.template_name]

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def form_valid(self, form):
        messages.info(self.request, 'Item has been saved!')
        return super(ItemEditView, self).form_valid(form)


class ItemCreateRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return "%s?next=%s" % (reverse_lazy('folioport:dashboard:cms:item-create',
            kwargs={'class_name': self.request.GET['class_name'],
                    'container_id': self.request.GET.get('container_id', 0)}),
        self.request.GET.get('next', ''))


class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/cms/item_create.html'

    def get_template_names(self):
        if self.model.get_edit_create_template():
            return [self.model.get_edit_create_template()]
        return [self.template_name]

    def get_form_class(self):
        if self.model.get_form_class():
            return self.model.get_form_class()
        return super(ItemCreateView, self).get_form_class()

    def dispatch(self, *args, **kwargs):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return super(ItemCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse_lazy('folioport:dashboard:cms:container-list')

    def form_valid(self, form):
        response = super(ItemCreateView, self).form_valid(form)
        self.object.assign_to_container(self.kwargs['container_id'])
        messages.info(self.request, 'Item has been created!')
        return response


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'dashboard/cms/item_delete.html'

    def get_queryset(self):
        self.model = models.get_model('cms', self.kwargs['class_name'])
        return self.model.objects.filter(id=self.kwargs['pk'])

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse_lazy('folioport:dashboard:cms:container-list')
