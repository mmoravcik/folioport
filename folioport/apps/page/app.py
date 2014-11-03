from django.conf.urls import patterns, url

from folioport.base.app import Application
from folioport.apps.page import views


class PageApplication(Application):
    name = 'page'
    page_view = views.PageDetailView
    page_preview = views.PagePreview

    def get_urls(self):
        urlpatterns = super(PageApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^(?P<page_slug>[\w-]*)-(?P<pk>\d+)/$', self.page_view.as_view(), name='detail'),
            url(r'^preview/(?P<page_slug>[\w-]*)-(?P<pk>\d+)/$', self.page_preview.as_view(), name='preview'),
        )
        return urlpatterns


application = PageApplication()