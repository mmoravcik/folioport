from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class CmsApplication(Application):
    name = 'cms'

    container_list_view = views.ContainerListView
    edit_container_view = views.ContainerEditView
    edit_item_view = views.ItemEditView
    create_item_view = views.ItemCreateView
    create_item_redirect_view = views.ItemCreateRedirectView
    create_view = views.PostCreateView
    delete_view = views.PostDeleteView

    def get_urls(self):
        urlpatterns = super(CmsApplication, self).get_urls()
        urlpatterns += patterns(
            '',
            url(r'/edit/(?P<pk>\d+)/$',
                self.edit_container_view.as_view(),
                name='container-edit'),

            url(r'/create_item_redirect/$',
                self.create_item_redirect_view.as_view(),
                name='item-create-redirect'),

            url(r'/create_item/(?P<container_id>\d+)/(?P<class_name>\w+)/$',
                self.create_item_view.as_view(),
                name='item-create'),

            url(r'/edit_item/(?P<class_name>\w+)/(?P<pk>\d+)/$',
                self.edit_item_view.as_view(),
                name='item-edit'),

            url(r'/delete/(?P<pk>\d+)/$',
                self.delete_view.as_view(),
                name='container-delete'),
            url(r'/create',
                self.create_view.as_view(),
                name='container-create'),
            url(r'',
                self.container_list_view.as_view(),
                name='container-list'),
        )
        return urlpatterns


application = CmsApplication()