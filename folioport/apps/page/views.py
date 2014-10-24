from django.db import models
from django.views.generic.detail import DetailView


Page = models.get_model('page', 'Page')


class PageDetailView(DetailView):
    template_name = 'pages/page.html'
    model = Page
    context_object_name = 'page'
    queryset = Page.site_objects.active()