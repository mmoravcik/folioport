from django.db import models
from django.views.generic.base import TemplateView

Project = models.get_model('project', 'Project')

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context['projects'] = Project.objects.filter(active=True).order_by('order')
        return context
