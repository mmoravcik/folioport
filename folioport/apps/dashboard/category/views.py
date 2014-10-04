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


class CategoryListView(FilterUserMixin, LoginRequiredMixin, ListView):
    template_name = 'dashboard/category/list.html'

    def get_queryset(self):
        Category = models.get_model(self.kwargs['app'], 'Category')
        return Category.objects.filter(user=self.request.user)


class CategoryEditView(FilterUserMixin, LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    template_name = 'dashboard/category/edit.html'

    def get_queryset(self):
        Category = models.get_model(self.kwargs['app'], 'Category')
        return Category.objects.filter(user=self.request.user)

    def get_form_class(self):
        Category = models.get_model(self.kwargs['app'], 'Category')
        return Category.get_form_class()

    def get_success_url(self):
        messages.success(self.request, 'Category has been saved!')
        return reverse_lazy('folioport:dashboard:category:list',
                            kwargs={'app': 'project'})

    def form_valid(self, form):
        return super(CategoryEditView, self).form_valid(form)


class CategoryCreateView(FilterUserMixin, LoginRequiredMixin, CreateView):
    template_name = 'dashboard/category/create.html'

    def get_success_url(self):
        return reverse_lazy('folioport:dashboard:category:list',
            kwargs={'app': 'project'})

    def get_queryset(self):
        Category = models.get_model(self.kwargs['app'], 'Category')
        return Category.objects.filter(user=self.request.user)

    def get_form_class(self):
        Category = models.get_model(self.kwargs['app'], 'Category')
        return Category.get_form_class()

    def form_valid(self, form):
        form.instance.site = get_current_site(self.request)
        form.instance.user = self.request.user
        messages.info(self.request, 'Category has been created!')
        return super(CategoryCreateView, self).form_valid(form)


class CategoryDeleteView(FilterUserMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'dashboard/category/delete.html'

    def get_queryset(self):
        Category = models.get_model(self.kwargs['app'], 'Category')
        return Category.objects.filter(user=self.request.user)

    def get_success_url(self):
        messages.info(self.request, 'Category has been deleted!')
        return reverse_lazy('folioport:dashboard:category:list',
                            kwargs={'app': 'project'})