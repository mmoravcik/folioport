from django.db import models

from folioport.apps.cms import abstract_models
from folioport.base.abstract_models import AbstractImage
from folioport.apps.cms.abstract_models import ContentItemMixin


class Container(abstract_models.AbstractContainer):
    pass


class Item(abstract_models.AbstractItem):
    pass


class ContainerItems(abstract_models.AbstractContainerItems):
    pass


class ItemText(abstract_models.AbstractItemText):
    pass


class ItemRichText(abstract_models.AbstractItemRichText):
    pass


class Image(ContentItemMixin, AbstractImage):
    @staticmethod
    def get_form_class():
        from forms import ImageForm
        return ImageForm


class GalleryImage(ContentItemMixin, AbstractImage):
    hover_image = models.ImageField(
        upload_to='hover_images', null=True, blank=True)

    @staticmethod
    def get_form_class():
        from forms import GalleryImageForm
        return GalleryImageForm


class ItemImage(abstract_models.AbstractItemImage):
    hover_image = models.ImageField(
        upload_to='single_hover_images', null=True, blank=True)


class ItemRandomImage(abstract_models.AbstractRandomImage):
    pass


class ItemEmbed(abstract_models.AbstractItemEmbed):
    pass


class ItemGallery(abstract_models.AbstractItemGallery):
    pass