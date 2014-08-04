from django.db import models

from folioport.apps.project.abstract_models import AbstractProject
from folioport.base.abstract_models import AbstractEmbed, AbstractImage,\
    AbstractCategory


class Category(AbstractCategory):
    pass


class HoverOnImage(AbstractImage):
    pass


class Image(AbstractImage):
    project = models.ForeignKey('project.Project')
    hover_on = models.ForeignKey('project.HoverOnImage',
        related_name='hover_on_image', blank=True, null=True)

class Project(AbstractProject):
    pass


class Embed(AbstractEmbed):
    project = models.ForeignKey('project.Project')