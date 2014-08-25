from django.db.models import get_model
from django.views.generic.base import TemplateView
from django.middleware.csrf import get_token

from ajaxuploader.views import AjaxFileUploader

Project = get_model('project', 'Project')
Container = get_model('cms', 'Container')


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context['projects'] = Project.objects.all()

        container = Container.objects.get(id=1)
        context['cms'] = container.render()
        return context


def start(request):
    csrf_token = get_token(request)
    return render_to_response('import.html',
            {'csrf_token': csrf_token}, context_instance = RequestContext(request))


import_uploader = AjaxFileUploader()