from django.db import models

from folioport.apps.project.abstract_models import AbstractProject
from folioport.base.abstract_models import AbstractEmbed, AbstractImage,\
    AbstractCategory


class Category(AbstractCategory):
    pass


class Image(AbstractImage):
    project = models.ForeignKey('project.Project')


class Project(AbstractProject):
    pass


class Embed(AbstractEmbed):
    project = models.ForeignKey('project.Project')