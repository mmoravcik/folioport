from django.db import models


class AbstractContainer(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        abstract = True

    def render(self):
        html = ''
        for item in self.item_set.all():
            Item = models.get_model('cms', item.item_class)
            item = Item.objects.get(pk=item.item_id)
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

    def __unicode__(self):
        return "%s - %s" % (self.container, self.item)

    class Meta:
        abstract = True


class AbstractItemText(models.Model):
    template = 'cms/content_items/text.html'
    text = models.TextField(default='')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.text

    def render(self):
        return self.text


class AbstractItemImage(models.Model):
    template = 'cms/content_items/image.html'
    image = models.ForeignKey('cms.Image')

    class Meta:
        abstract = True


    def render(self):
        return str(self.image.image)
