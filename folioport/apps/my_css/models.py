from my_css.abstract_models import AbstractMyCSS, AbstractMyCSSArchive
from my_css import settings as css_settings

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site


class MyCSS(AbstractMyCSS):
    site = models.ForeignKey(Site)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def archive(self):
        if css_settings.MY_CSS_ARCHIVE_LIFE:
            MyCSSArchive = models.get_model('my_css', 'MyCSSArchive')
            MyCSSArchive.objects.create(
                css=self.css, user=self.user, site=self.user.site)


class MyCSSArchive(AbstractMyCSSArchive):
    site = models.ForeignKey(Site)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ('-date_created',)


from my_css.models import *