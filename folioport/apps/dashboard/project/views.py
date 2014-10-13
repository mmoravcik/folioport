from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages

from folioport.base.mixins import LoginRequiredMixin, FilterUserMixin, \
    AjaxableResponseMixin, ObjectSaveMixin
from folioport.apps.project import forms

Project = models.get_model('project', 'Project')


class ProjectListView(FilterUserMixin, LoginRequiredMixin, ListView):
    template_name = 'dashboard/project/list.html'
    model = Project


class ProjectEditView(FilterUserMixin, LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Project
    form_class = forms.ProjectForm
    template_name = 'dashboard/project/edit.html'

    def get_success_url(self):
        messages.success(self.request, 'Project has been saved')
        return reverse_lazy('folioport:dashboard:project:edit',
                            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super(ProjectEditView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(ProjectEditView, self).get_context_data(**kwargs)
        if self.request.POST and not kwargs['form'].is_valid():
            ctx['active_tab'] = 'settings-tab'
        return ctx


class ProjectCreateView(FilterUserMixin, LoginRequiredMixin, CreateView):
    model = Project
    form_class = forms.ProjectForm
    template_name = 'dashboard/project/create.html'

    def get_form(self, form_class):
        form = super(ProjectCreateView, self).get_form(form_class)
        form.fields['category'].queryset = form.fields['category'].queryset.\
            filter(user=self.request.user)
        return form

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:project:edit',
            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.site = self.request.user.site
        messages.info(self.request, 'Project has been created!')
        return super(ProjectCreateView, self).form_valid(form)


class ProjectDeleteView(FilterUserMixin, LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'dashboard/project/delete.html'

    def get_success_url(self):
        messages.info(self.request, 'Project has been deleted!')
        return reverse_lazy('folioport:dashboard:project:list')


class ProjectOrderSaveView(ObjectSaveMixin):
    model = Project