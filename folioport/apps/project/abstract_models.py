from tagging.fields import TagField
from tagging.models import Tag, TaggedItem

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from folioport.base.utils import get_solr_thumbnail_geometry


class ProjectManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(active=True)


class SiteProjectManager(ProjectManager, CurrentSiteManager):
    pass


class AbstractProject(models.Model):
    JPEG, PNG, GIF = "JPEG", "PNG", "GIF"

    THUMBNAIL_TYPE_CHOICE = (
        (JPEG, 'jpeg'),
        (PNG, 'png'),
        (GIF, 'gif'),
    )

    site = models.ForeignKey(Site)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=128)
    category = models.ManyToManyField('project.Category', blank=True)
    slug = models.SlugField(help_text='Text to be displayed in URL', max_length=128,
                            default='', blank=True)
    active = models.BooleanField(default=True)
    release_date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='images/project_thumbnails')
    thumbnail_height = models.IntegerField(default=0)
    thumbnail_width = models.IntegerField(default=250)
    thumbnail_type = models.CharField(
        max_length=4, choices=THUMBNAIL_TYPE_CHOICE, default=JPEG)
    order = models.IntegerField(default=0, null=True, blank=True)
    container = models.ForeignKey('cms.Container', null=True, blank=True)

    # TODO review tagging
    tags = TagField()

    class Meta:
        abstract = True
        ordering = ['order']

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.order)

    def get_absolute_url(self):
        return reverse(
            'folioport:project:detail', args=[self.slug, self.id])

    def get_preview_url(self):
        return reverse('folioport:project:preview', args=[self.slug, self.id])

    def get_solr_thumbnail_geometry(self):
        return get_solr_thumbnail_geometry(
            self.thumbnail_width, self.thumbnail_height)

    # TODO should be using get instead of filter in these queries?
    def next(self, category_slug=None):
        qs = self._get_filterered_qs(category_slug)
        p = qs.filter(order__gte=self.order).order_by('order', 'pk')
        if not p:
            p = qs.order_by('order', 'pk')
        return p[0] if p else None

    def previous(self, category_slug=None):
        qs = self._get_filterered_qs(category_slug)
        p = qs.filter(order__lte=self.order).order_by('-order', '-pk')
        if not p:
            p = qs.order_by('-order', '-pk')
        return p[0] if p else None

    def _get_filterered_qs(self, category_slug=None):
        Project = models.get_model('project', 'Project')
        Category = models.get_model('project', 'Category')
        if category_slug:
            categories = Category.objects.active().filter(slug=category_slug)
            if categories:
                return Project.site_objects.active().filter(
                    category__in=[categories[0]]).exclude(id=self.id)

        return Project.site_objects.active().exclude(id=self.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(u'%s' % self.title)
        super(AbstractProject, self).save(*args, **kwargs)
        if self.container is None:
            Container = models.get_model('cms', 'Container')
            container = Container.objects.create(
                user=self.user, title=self.title)
            self.container = container
            self.container.user = self.user
            self.save()

    def delete(self):
        if self.container:
            self.container.delete()
        return super(AbstractProject, self).delete()

    # Tagging
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def related_projects(self, limit=3):
        objects = TaggedItem.objects.get_related(self, self.__class__)
        return objects[:limit]

    objects = ProjectManager()
    site_objects = SiteProjectManager()
