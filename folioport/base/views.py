from django.db.models import get_model
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

Project = get_model('project', 'Project')
Page = get_model('page', 'Page')


class HomeView(TemplateView):
    template_name = 'home.html'
    landing_page = None

    def get(self, request, *args, **kwargs):
        landing_pages = Page.site_objects.active().filter(type=Page.LANDING_PAGE)
        if landing_pages:
            self.landing_page = landing_pages[0]
        else:
            projects = Project.site_objects.all().order_by('?')
            if projects:
                return HttpResponseRedirect(projects[0].get_absolute_url())
        return super(HomeView, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        if self.landing_page:
            context['page'] = self.landing_page
        return context
