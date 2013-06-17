from django.db.models import get_model
from django.views.generic.base import TemplateView

Project = get_model('project', 'Project')


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context['projects'] = Project.active_objects.all()
        return context