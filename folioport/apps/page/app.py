from django.conf.urls import patterns, url

from folioport.base.app import Application
from folioport.apps.page import views


class PageApplication(Application):
    name = 'page'
    post_view = views.PageDetailView

    def get_urls(self):
        urlpatterns = super(PageApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^(?P<page_slug>[\w-]*)-(?P<pk>\d+)/$', self.post_view.as_view(), name='detail'),
        )
        return urlpatterns


application = PageApplication()