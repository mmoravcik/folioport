from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.sites.models import get_current_site

from folioport.base.mixins import LoginRequiredMixin, FilterUserMixin, \
    AjaxableResponseMixin, ObjectSaveMixin
from folioport.apps.page.forms import PageForm

Page = models.get_model('page', 'Page')


class PageListView(FilterUserMixin, LoginRequiredMixin, ListView):
    template_name = 'dashboard/page/list.html'
    model = Page


class PageEditView(FilterUserMixin, LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'dashboard/page/edit.html'

    def get_success_url(self):
        messages.success(self.request, 'Page has been saved')
        return reverse_lazy('folioport:dashboard:page:edit',
                            kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     return super(PageEditView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(PageEditView, self).get_context_data(**kwargs)
        if self.request.POST and not kwargs['form'].is_valid():
            ctx['active_tab'] = 'settings-tab'
        return ctx


class PageCreateView(FilterUserMixin, LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'dashboard/page/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:page:edit',
            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.site = get_current_site(self.request)
        messages.info(self.request, 'Page has been created!')
        return super(PageCreateView, self).form_valid(form)


class PageDeleteView(FilterUserMixin, LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'dashboard/page/delete.html'

    def get_success_url(self):
        messages.info(self.request, 'Page has been deleted!')
        return reverse_lazy('folioport:dashboard:page:list')


class PageOrderSaveView(ObjectSaveMixin):
    model = Page