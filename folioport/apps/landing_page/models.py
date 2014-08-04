from django.db import models

from folioport.apps.landing_page.abstract_models import AbstractLandingPage
from folioport.base.abstract_models import AbstractEmbed, AbstractImage


class LandingPage(AbstractLandingPage):
    pass


class Image(AbstractImage):
    landing_page = models.ForeignKey('landing_page.LandingPage')


class Embed(AbstractEmbed):
    landing_page = models.ForeignKey('landing_page.LandingPage')