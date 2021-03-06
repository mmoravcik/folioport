from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.utils.text import slugify


class PageManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(active=True)


class SitePageManager(PageManager, CurrentSiteManager):
    pass


class AbstractPage(models.Model):
    LANDING_PAGE, CONTENT_PAGE = 1, 2
    TYPE_CHOICES = (
        (LANDING_PAGE, 'Landing page'),
        (CONTENT_PAGE, 'Standard page')
    )

    site = models.ForeignKey(Site)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=128)
    slug = models.SlugField(help_text='Text to be displayed in URL',
                            max_length=128, default='', blank=True)
    active = models.BooleanField(default=True)
    order = models.IntegerField(null=True, blank=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=CONTENT_PAGE)
    container = models.ForeignKey('cms.Container', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['order']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('folioport:page:detail', args=[self.slug, self.id])

    def get_preview_url(self):
        return reverse('folioport:page:preview', args=[self.slug, self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(u'%s' % self.title)
        super(AbstractPage, self).save(*args, **kwargs)
        if self.container is None:
            Container = models.get_model('cms', 'Container')
            container = Container.objects.create(
                user=self.user, title=self.title)
            self.container = container
            self.save()

    def delete(self):
        if self.container:
            self.container.delete()
        return super(AbstractPage, self).delete()

    def get_absolute_url(self):
        return reverse('folioport:page:detail', args=[self.slug, self.id])

    objects = PageManager()
    site_objects = SitePageManager()
