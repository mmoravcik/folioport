from folioport.apps.cms import abstract_models
from folioport.base.abstract_models import AbstractImage


class Container(abstract_models.AbstractContainer):
    pass


class Item(abstract_models.AbstractItem):
    pass


class ContainerItems(abstract_models.AbstractContainerItems):
    pass


class ItemText(abstract_models.AbstractItemText):
    pass


class Image(AbstractImage):
    pass


class ItemImage(abstract_models.AbstractItemImage):
    pass