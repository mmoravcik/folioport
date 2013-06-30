from django.db import models
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist

MyCSS = models.get_model('mycss', 'MyCSS')


class MyCSSView(DetailView):
    pass