from django.db import models


class AbstractLandingPage(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return '%s' % self.name

    def get_images(self):
        return self.image_set.all().order_by('?')

    def get_embeds(self):
        return self.embed_set.all().order_by('?')



