from django.db import models

from folioport.models import CommonInfo

class AbstractNews(CommonInfo):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
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