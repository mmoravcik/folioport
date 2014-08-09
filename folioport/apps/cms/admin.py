from django.db.models import get_model
from django.contrib import admin

Container = get_model('cms', 'Container')
ContainerItems = get_model('cms', 'ContainerItems')
Item = get_model('cms', 'Item')
ItemText = get_model('cms', 'ItemText')
ItemImage = get_model('cms', 'ItemImage')
Image = get_model('cms', 'Image')

admin.site.register(Container)
admin.site.register(ContainerItems)
admin.site.register(Item)
admin.site.register(ItemText)
admin.site.register(ItemImage)
admin.site.register(Image)
