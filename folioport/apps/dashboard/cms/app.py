from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class CmsApplication(Application):
    name = 'cms'

    edit_item_view = views.ItemEditView
    create_item_view = views.ItemCreateView
    delete_item_view = views.ItemDeleteView
    create_item_redirect_view = views.ItemCreateRedirectView
    items_order_save_view = views.ItemsOrderSave
    container_preview_view = views.ContainerPreviewView

    def get_urls(self):
        urlpatterns = super(CmsApplication, self).get_urls()
        urlpatterns += patterns(
            '',
            url(r'/create_item_redirect/$',
                self.create_item_redirect_view.as_view(),
                name='item-create-redirect'),

            url(r'/create_item/(?P<container_id>\d+)/(?P<class_name>\w+)/$',
                self.create_item_view.as_view(),
                name='item-create'),

            url(r'/edit_item/(?P<class_name>\w+)/(?P<pk>\d+)/$',
                self.edit_item_view.as_view(),
                name='item-edit'),

            url(r'/delete_item/(?P<class_name>\w+)/(?P<pk>\d+)/$',
                self.delete_item_view.as_view(),
                name='item-delete'),
            url(r'/items_order_save/$',
                self.items_order_save_view.as_view(),
                name='items-order-save'),
            url(r'/container_preview/(?P<container_id>\d+)/$',
                self.container_preview_view.as_view(),
                name='container-preview'),
        )
        return urlpatterns


application = CmsApplication()