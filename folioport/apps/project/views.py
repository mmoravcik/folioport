from django.db import models
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist

Project = models.get_model('project', 'Project')
Category = models.get_model('project', 'Category')


class ProjectView(DetailView):
    template_name = 'pages/project.html'
    model = Project
    context_name = 'project'
    queryset = Project.site_objects.active()

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        category_slug = self.request.GET.get('cat', None)
        category = get_category_by_slug(category_slug)
        context['category'] = category
        context['next_project'] = self.get_object().next(category_slug)
        context['previous_project'] = self.get_object().previous(category_slug)
        return context


# TODO check this for site filter
class CategoryView(TemplateView):
    template_name = 'pages/project_category.html'
       
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        category = get_category_by_slug(self.kwargs['category_slug'])
        context['projects'] = Project.objects.active().filter(category=category).order_by('order')
        context['category'] = category
        return context


def get_category_by_slug(category_slug):
    try:
        return Category.objects.get(slug=category_slug)
    except ObjectDoesNotExist:
        return None