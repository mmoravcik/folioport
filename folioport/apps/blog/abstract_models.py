import datetime

from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify


class BlogManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(active=True)


class SiteBlogManager(BlogManager, CurrentSiteManager):
    pass


class AbstractPost(models.Model):
    site = models.ForeignKey(Site)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=128)
    slug = models.SlugField(help_text='Text to be displayed in URL',
                            default='', blank=True, max_length=128)
    active = models.BooleanField(default=True)
    release_date = models.DateTimeField(
        'Date posted', default=datetime.datetime.now(), null=True, blank=True)
    order = models.IntegerField(default=0, null=True, blank=True)
    container = models.ForeignKey('cms.Container', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-release_date']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(u'%s' % self.title)

        # if we don't have time, add some so previous / next works
        if self.release_date.time() == datetime.time.min:
            self.release_date = self.release_date + \
                datetime.timedelta(
                    seconds=datetime.datetime.now().time().second,
                    microseconds=datetime.datetime.now().time().microsecond,
                    minutes=datetime.datetime.now().time().minute,
                    hours=datetime.datetime.now().time().hour,
                )

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

    # TODO should be using get instead of filter in these queries?
    def next(self):
        Post = models.get_model('blog', 'Post')
        qs = Post.site_objects.active().exclude(id=self.id)
        p = qs.filter(release_date__gte=self.release_date).\
            order_by('release_date', 'pk')
        return p[0] if p else None

    def previous(self, category_slug=None):
        Post = models.get_model('blog', 'Post')
        qs = Post.site_objects.active().exclude(id=self.id)
        p = qs.filter(release_date__lte=self.release_date).\
            order_by('-release_date', '-pk')
        return p[0] if p else None

    objects = BlogManager()
    site_objects = SiteBlogManager()