from django.core.urlresolvers import reverse
from django.db import models


class AbstractPage(models.Model):
    LANDING_PAGE, CONTENT_PAGE = 1, 2
    TYPE_CHOICES = (
        (LANDING_PAGE, 'Landing page'),
        (CONTENT_PAGE, 'Standard page')
    )

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    active = models.BooleanField(default=True)
    order = models.IntegerField(null=True, blank=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=CONTENT_PAGE)
    container = models.ForeignKey('cms.Container', null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(AbstractPage, self).save(*args, **kwargs)
        if self.container is None:
            Container = models.get_model('cms', 'Container')
            container = Container.objects.create(title=self.title)
            self.container = container
            self.save()

    def delete(self):
        if self.container:
            self.container.delete()
        return super(AbstractPage, self).delete()

    def get_absolute_url(self):
        return reverse('folioport:page:detail', args=[self.slug, self.id])
