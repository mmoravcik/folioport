from django.db import models
from django.views.generic.detail import DetailView

from folioport.base.mixins import FilterSiteMixin

Page = models.get_model('page', 'Page')


class PageDetailView(FilterSiteMixin, DetailView):
    template_name = 'pages/page.html'
    model = Page
