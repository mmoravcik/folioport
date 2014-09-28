from datetime import datetime

from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class BlogManager(CurrentSiteManager):
    def active(self):
        return self.get_query_set().filter(active=True)


class AbstractPost(models.Model):
    site = models.ForeignKey(Site)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    active = models.BooleanField(default=True)
    release_date = models.DateField(
        'Date posted', default=datetime.now(), null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    container = models.ForeignKey('cms.Container', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['order', '-release_date']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(AbstractPost, self).save(*args, **kwargs)
        if self.container is None:
            Container = models.get_model('cms', 'Container')
            container = Container.objects.create(
                title=self.title, user=self.user)
            self.container = container
            self.save()

    def delete(self):
        if self.container:
            self.container.delete()
        return super(AbstractPost, self).delete()

    def get_absolute_url(self):
        return reverse('folioport:blog:post-detail', args=[self.slug, self.id])

    objects = BlogManager()