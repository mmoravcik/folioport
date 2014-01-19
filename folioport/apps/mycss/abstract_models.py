from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class AbstractMyCSS(models.Model):
    css = models.TextField(default="", blank=True)

    def save(self):
        super(AbstractMyCSS, self).save()

        filename = 'mycss.css'
        path = settings.MYCSS_ROOT + filename

        if default_storage.exists(path):
            default_storage.delete(path)
        default_storage.save(path, ContentFile(self.css))

    class Meta:
        abstract = True