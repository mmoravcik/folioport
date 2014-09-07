from django.db.models import get_model
from django.views.generic.base import TemplateView

Project = get_model('project', 'Project')
Page = get_model('page', 'Page')


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        landing_pages = Page.on_site.filter(type=Page.LANDING_PAGE)
        if landing_pages:
            context['page'] = landing_pages[0]
        context['projects'] = Project.on_site.all()

        return context
