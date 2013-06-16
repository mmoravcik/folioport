from django.db import models


class AbstractNews(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, default='')
    body = models.TextField()
    active = models.BooleanField(default=True)
    release_date = models.DateTimeField()
    
    def get_absolute_url(self):
        return ('/news/%s' % self.slug)
    
    class Meta:
        ordering = ['-release_date']
        abstract = True
    
    def __unicode__(self):
        return self.title