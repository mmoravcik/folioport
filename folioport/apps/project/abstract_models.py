from tagging.fields import TagField
from tagging.models import Tag, TaggedItem

from mptt.models import MPTTModel, TreeForeignKey

from djangoratings.fields import AnonymousRatingField

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Max

from folioport.base.utils import get_solr_thumbnail_geometry


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(active=True)


class AbstractCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=128)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

    objects = models.Manager()
    active_objects = ActiveCategoryManager()


class AbstractMedia(models.Model):
    project = models.ForeignKey('project.Project')
    caption = models.TextField(blank=True)
    width = models.IntegerField(default=300)
    height = models.IntegerField(default=0)
    order = models.IntegerField(default=1)

    class Meta:
        abstract = True


class AbstractEmbed(AbstractMedia):
    embed_code = models.TextField()

    def __unicode__(self):
        return self.caption

    class Meta:
        abstract = True


class AbstractImage(AbstractMedia):
    JPEG, PNG = "JPEG","PNG"

    THUMBNAIL_TYPE_CHOICE = (
        (JPEG, 'jpeg'),
        (PNG, 'png'),
    )

    image = models.ImageField(upload_to='images/project_images')
    thumbnail_type = models.CharField(max_length=4, choices=THUMBNAIL_TYPE_CHOICE, default=JPEG)

    def get_solr_thumbnail_geometry(self):
        return get_solr_thumbnail_geometry(self.width, self.height)

    def __unicode__(self):
        return self.image.name

    class Meta:
        abstract = True


class ActiveProjectManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProjectManager, self).get_query_set().filter(active=True)


class AbstractProject(models.Model):
    JPEG, PNG = "JPEG", "PNG"

    THUMBNAIL_TYPE_CHOICE = (
        (JPEG, 'jpeg'),
        (PNG, 'png'),
    )

    name = models.CharField(max_length=128)
    category = models.ManyToManyField('project.Category')
    slug = models.SlugField(max_length=128)
    active = models.BooleanField(default=True)
    summary = models.TextField(default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/project_thumbnails')
    thumbnail_height = models.IntegerField(default=0)
    thumbnail_width = models.IntegerField(default=100)
    thumbnail_type = models.CharField(max_length=4, choices=THUMBNAIL_TYPE_CHOICE, default=JPEG)
    order = models.IntegerField(null=True, blank=True)

    #todo review tagging
    tags = TagField()
    #todo review rating
    rating = AnonymousRatingField(range=10, can_change_vote=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.order)

    def get_images(self):
        return self.image_set.all().order_by('order')

    def get_embeds(self):
        return self.embed_set.all().order_by('order')

    def get_absolute_url(self):
        return reverse('folioport:project:project-detail', args=[self.slug, self.id])

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def get_rating(self):
        return int(round(self.rating.get_rating(), 0))

    def get_solr_thumbnail_geometry(self):
        return get_solr_thumbnail_geometry(self.thumbnail_width, self.thumbnail_height)

    def related_projects(self, limit=3):
        objects = TaggedItem.objects.get_related(self, self.__class__)
        return objects[:limit]

    #todo should be using get instead of filter in these queries?
    def next(self, category_slug = None):
        qs = self._get_filterered_qs(category_slug)
        p = qs.filter(order__gte=self.order).order_by('order','pk')
        if not p:
            p = qs.order_by('order','pk')
        return p[0] if p else None;

    def previous(self, category_slug = None):
        qs = self._get_filterered_qs(category_slug)
        p = qs.filter(order__lte=self.order).order_by('-order','-pk')
        if not p:
            p = qs.order_by('-order','-pk')
        return p[0] if p else None;

    def _get_filterered_qs(self, category_slug = None):
        Project = models.get_model('project', 'Project')
        Category = models.get_model('project', 'Category')
        if category_slug:
            categories = Category.active_objects.filter(slug=category_slug)
            if categories:
                return Project.active_objects.filter(category=categories[0]).exclude(id=self.id)

        return Project.active_objects.all().exclude(id=self.id)

    class Meta:
        abstract = True
        ordering = ['order']

    def save(self, *args, **kwargs):
        super(AbstractProject, self).save(*args, **kwargs)
        if self.order is None:
            Project = models.get_model('project', 'Project')
            max_order = Project.objects.all().aggregate(Max('order'))['order__max']
            if not max_order: max_order = 1
            self.order = max_order + 10
            self.save()

    objects = models.Manager()
    active_objects = ActiveProjectManager()