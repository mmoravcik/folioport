from django.db import models
from django.template import loader, Context

from folioport.base import abstract_models


class AbstractContainer(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        abstract = True

    def get_items(self):
        items = []
        for item in self.item_set.all().order_by('containeritems__position'):
            Item = models.get_model('cms', item.item_class)
            item_object = Item.objects.get(pk=item.item_id)
            item_object.class_name = item.item_class
            if item.template:
                item_object.template = item.template
            items.append(item_object)
        return items

    def render(self):
        html = ''
        for item in self.get_items():
            html += item.render()
        return html


class AbstractItem(models.Model):
    item_class = models.CharField(max_length=128)
    template = models.CharField(max_length=256, default='', blank=True)
    item_id = models.IntegerField(default=0)
    container = models.ManyToManyField('Container', through='ContainerItems')

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s - %s" % (self.item_class, self.item_id)


class AbstractContainerItems(models.Model):
    container = models.ForeignKey('Container')
    item = models.ForeignKey('Item')
    position = models.SmallIntegerField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s - %s" % (self.container, self.item)


class AbstractItemText(models.Model):
    template = 'cms/content_items/text.html'
    text = models.TextField(default='')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.text

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'text': self.text})
        return t.render(c)


class AbstractItemImage(abstract_models.AbstractImage):
    template = 'cms/content_items/image.html'

    class Meta:
        abstract = True

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'image': self})
        return t.render(c)


class AbstractRandomImage(models.Model):
    template = 'cms/content_items/random_image.html'
    image = models.ManyToManyField('cms.Image')

    class Meta:
        abstract = True

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'image': self.image.all().order_by('?')[0]})
        return t.render(c)