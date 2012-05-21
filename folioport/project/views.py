from django.db import models
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

Project = models.get_model('project', 'Project')
Category = models.get_model('project', 'Category')

class ProjectView(DetailView):
    template_name = 'pages/project.html'
    model = Project
    context_name = 'project'

    
class CategoryView(TemplateView):
    template_name = 'home.html'
       
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        context['projects'] = Project.objects.filter(active=True, category=category).order_by('order')
        return context
