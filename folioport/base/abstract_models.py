from django.db import models
from django.template.defaultfilters import slugify

from mptt.models import MPTTModel, TreeForeignKey

from folioport.base.utils import get_solr_thumbnail_geometry


class CategoryManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(active=True)


class AbstractCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=128, blank=True, default="")
    parent = TreeForeignKey('self', null=True, blank=True,
        related_name='children')
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(AbstractCategory, self).save(*args, **kwargs)

    objects = CategoryManager()


class AbstractMedia(models.Model):
    caption = models.CharField(max_length=128, blank=True)
    order = models.IntegerField(default=1)

    class Meta:
        abstract = True


class AbstractEmbed(AbstractMedia):
    AUDIO, VIDEO, OTHER = 1, 2, 3

    TYPE_CHOICES = (
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
        (OTHER, 'Other'),
        )

    embed_code = models.TextField()
    width = models.IntegerField(default=300)
    height = models.IntegerField(default=0)
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=VIDEO)

    def __unicode__(self):
        return self.caption

    class Meta:
        abstract = True


class AbstractImage(AbstractMedia):
    JPEG, PNG, GIF = "JPEG","PNG", "GIF"

    THUMBNAIL_TYPE_CHOICE = (
        (JPEG, 'jpeg'),
        (PNG, 'png'),
        (GIF, 'gif'),
        )

    image = models.ImageField(upload_to='images')
    thumbnail_type = models.CharField(
        max_length=4, choices=THUMBNAIL_TYPE_CHOICE, default=JPEG)
    width = models.IntegerField(default=300)
    height = models.IntegerField(default=0)

    def get_solr_thumbnail_geometry(self):
        return get_solr_thumbnail_geometry(self.width, self.height)

    def __unicode__(self):
        return self.image.name

    class Meta:
        abstract = True


class AbstractAudio(AbstractMedia):
    file = models.FileField(upload_to='audio')

    def __unicode__(self):
        return self.caption

    class Meta:
        abstract = True


class AbstractVideo(AbstractMedia):
    file = models.FileField(upload_to='video')

    def __unicode__(self):
        return self.caption

    class Meta:
        abstract = True