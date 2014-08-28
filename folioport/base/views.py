from django.db.models import get_model
from django.views.generic.base import TemplateView
from django.middleware.csrf import get_token

from ajaxuploader.views import AjaxFileUploader

Project = get_model('project', 'Project')
Page = get_model('page', 'Page')


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        landing_pages = Page.objects.filter(type=Page.LANDING_PAGE)
        if landing_pages:
            context['page'] = landing_pages[0]
        context['projects'] = Project.objects.all()

        return context


def start(request):
    csrf_token = get_token(request)
    return render_to_response('import.html',
            {'csrf_token': csrf_token}, context_instance = RequestContext(request))


import_uploader = AjaxFileUploader()