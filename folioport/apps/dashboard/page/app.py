from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class PageApplication(Application):
    name = 'page'

    list_view = views.PageListView
    edit_view = views.PageEditView
    create_view = views.PageCreateView
    delete_view = views.PageDeleteView

    def get_urls(self):
        urlpatterns = super(PageApplication, self).get_urls()
        urlpatterns += patterns(
            '',
            url(r'/edit/(?P<pk>\d+)/$',
                self.edit_view.as_view(),
                name='edit'),
            url(r'/delete/(?P<pk>\d+)/$',
                self.delete_view.as_view(),
                name='delete'),
            url(r'/create',
                self.create_view.as_view(),
                name='create'),
            url(r'',
                self.list_view.as_view(),
                name='list'),
        )
        return urlpatterns


application = PageApplication()