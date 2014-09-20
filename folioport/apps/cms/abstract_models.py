from django.conf import settings
from django.db import models
from django.template import loader, Context
from django.utils.html import mark_safe

from folioport.base import abstract_models


class AbstractContainer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        abstract = True

    def get_item_objects(self):
        items = []
        for item in self.get_items():
            Item = models.get_model('cms', item.item_class)
            item_object = Item.objects.get(pk=item.item_id)
            item_object.class_name = item.item_class
            if item.template:
                item_object.template = item.template
            item_object.container_item = item
            items.append(item_object)
        return items

    def get_items(self):
        return self.item_set.all().order_by('containeritems__position')

    def delete(self):
        for item in self.get_items():
            item.delete()
        return super(AbstractContainer, self).delete()

    def render(self):
        html = ''
        for item in self.get_item_objects():
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


class ContentItemMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    class Meta:
        abstract = True

    @staticmethod
    def get_form_class():
        return None

    @staticmethod
    def get_edit_create_template():
        return None

    def render(self):
        return ""

    def assign_to_user(self, user):
        self.user = user
        self.save()

    def assign_to_container(self, container_id, position=100):
        if container_id and container_id != '0':
            Item = models.get_model('cms', 'Item')
            Container = models.get_model('cms', 'Container')
            ContainerItems = models.get_model('cms', 'ContainerItems')
            new_item, created = Item.objects.get_or_create(
                item_class=self.__class__.__name__, item_id=self.id)
            container = Container.objects.get(pk=container_id)
            ContainerItems.objects.create(
                container=container, item=new_item, position=position)

    def delete(self):
        Item = models.get_model('cms', 'Item')
        Item.objects.filter(
            item_class=self.__class__.__name__, item_id=self.pk).delete()
        super(ContentItemMixin, self).delete()


class AbstractItemText(ContentItemMixin):
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


class AbstractItemRichText(ContentItemMixin):
    template = 'cms/content_items/rich_text.html'
    text = models.TextField(default='')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.text

    @staticmethod
    def get_form_class():
        from forms import ItemRichTextForm
        return ItemRichTextForm

    @staticmethod
    def get_edit_create_template():
        return 'cms/content_items/admin/rich_text.html'

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'text': mark_safe(self.text)})
        return t.render(c)


class AbstractItemImage(ContentItemMixin, abstract_models.AbstractImage):
    template = 'cms/content_items/image.html'

    class Meta:
        abstract = True

    @staticmethod
    def get_form_class():
        from forms import ItemImageForm
        return ItemImageForm

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'image': self})
        return t.render(c)


class AbstractItemEmbed(ContentItemMixin, abstract_models.AbstractEmbed):
    template = 'cms/content_items/embed.html'

    class Meta:
        abstract = True

    @staticmethod
    def get_form_class():
        from forms import ItemEmbedForm
        return ItemEmbedForm

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'embed': self})
        return t.render(c)


class AbstractRandomImage(ContentItemMixin):
    template = 'cms/content_items/random_image.html'
    image = models.ManyToManyField('cms.Image')

    @staticmethod
    def get_form_class():
        from forms import ItemRandomImageForm
        return ItemRandomImageForm

    class Meta:
        abstract = True

    @staticmethod
    def get_edit_create_template():
        return 'cms/content_items/admin/random_image.html'

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'image': self.image.all().order_by('?')[0]})
        return t.render(c)


class AbstractItemGallery(ContentItemMixin):
    template = 'cms/content_items/gallery.html'
    image = models.ManyToManyField('cms.GalleryImage')

    class Meta:
        abstract = True

    @staticmethod
    def get_form_class():
        from forms import ItemGalleryForm
        return ItemGalleryForm

    @staticmethod
    def get_edit_create_template():
        return 'cms/content_items/admin/gallery.html'

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'images': self.image.all()})
        return t.render(c)


class AbstractItemHeading(ContentItemMixin):
    template = 'cms/content_items/heading.html'
    text = models.CharField(max_length=256, default="")
    level = models.PositiveSmallIntegerField(default=2)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s (level %s)" % (self.text, self.level)

    def render(self):
        t = loader.get_template(self.template)
        c = Context({'text': mark_safe(self.text),
                     'level': self.level})
        return t.render(c)