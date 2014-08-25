from django.core.urlresolvers import reverse
from django.db import models


class AbstractPost(models.Model):
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
        super(AbstractPost, self).save(*args, **kwargs)
        if self.container is None:
            Container = models.get_model('cms', 'Container')
            container = Container.objects.create(title=self.title)
            self.container = container
            self.save()

    def get_absolute_url(self):
        return reverse('folioport:blog:post-detail', args=[self.slug, self.id])
