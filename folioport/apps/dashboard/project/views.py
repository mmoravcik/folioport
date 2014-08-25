from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages

from folioport.base.mixins import LoginRequiredMixin
from folioport.apps.project import forms

Project = models.get_model('project', 'Project')


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/project/list.html'
    model = Project


class ProjectEditView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = forms.ProjectForm
    template_name = 'dashboard/project/edit.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:project:list')

    def form_valid(self, form):
        messages.info(self.request, 'Project has been saved!')
        return super(ProjectEditView, self).form_valid(form)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = forms.ProjectForm
    template_name = 'dashboard/project/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:project:edit',
            kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.info(self.request, 'Project has been created!')
        return super(ProjectCreateView, self).form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'dashboard/project/delete.html'

    def get_success_url(self):
        messages.info(self.request, 'Project has been deleted!')
        return reverse_lazy('folioport:dashboard:project:list')