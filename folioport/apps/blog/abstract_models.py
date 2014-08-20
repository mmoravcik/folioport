from tagging.fields import TagField
from tagging.models import Tag, TaggedItem

from mptt.models import MPTTModel, TreeForeignKey

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Max


class ActivePostManager(models.Manager):
    def get_query_set(self):
        return super(ActivePostManager, self).get_query_set().filter(active=True)



class AbstractBlogPost(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    active = models.BooleanField(default=True)
    release_date = models.DateField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    container = models.ForeignKey('cms.Container', null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(AbstractBlogPost, self).save(*args, **kwargs)
        if self.container is None:
            Container = models.get_model('cms', 'Container')
            container = Container.objects.create(title=self.title)
            self.container = container
            self.save()

    def get_absolute_url(self):
        return reverse('folioport:blog:post-detail', args=[self.slug, self.id])



class AbstractPost(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    active = models.BooleanField(default=True)
    content = models.TextField(default="", null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/blog_thumbnails')
    order = models.IntegerField(null=True, blank=True)

    #todo review tagging
    tags = TagField()

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.order)

    def get_absolute_url(self):
        return reverse('folioport:blog:post-detail', args=[self.slug, self.id])

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def related_posts(self, limit=3):
        objects = TaggedItem.objects.get_related(self, self.__class__)
        return objects[:limit]

    class Meta:
        abstract = True
        ordering = ['order']

    def save(self, *args, **kwargs):
        super(AbstractPost, self).save(*args, **kwargs)
        if self.order is None:
            Post = models.get_model('blog', 'Post')
            max_order = Post.objects.all().aggregate(Max('order'))['order__max']
            if not max_order: max_order = 1
            self.order = max_order + 10
            self.save()

    objects = models.Manager()
    active_objects = ActivePostManager()