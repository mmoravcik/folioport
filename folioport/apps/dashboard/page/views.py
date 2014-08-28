from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages

from folioport.base.mixins import LoginRequiredMixin
from folioport.apps.page.forms import PageForm

Page = models.get_model('page', 'Page')


class PageListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/page/list.html'
    model = Page


class PageEditView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'dashboard/page/edit.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:page:list')

    def form_valid(self, form):
        messages.info(self.request, 'Page has been saved!')
        return super(PageEditView, self).form_valid(form)


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'dashboard/page/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:page:edit',
            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.info(self.request, 'Page has been created!')
        return super(PageCreateView, self).form_valid(form)


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'dashboard/page/delete.html'

    def get_success_url(self):
        messages.info(self.request, 'Page has been deleted!')
        return reverse_lazy('folioport:dashboard:page:list')