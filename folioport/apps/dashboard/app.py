from django.conf.urls import patterns, url, include

from folioport.base.app import Application
from folioport.apps.dashboard.blog.app import application as blog_app
from folioport.apps.dashboard.cms.app import application as cms_app
from folioport.apps.dashboard.project.app import application as project_app

from . import views


class DashboardApplication(Application):
    name = 'dashboard'
    blog_app = blog_app
    cms_app = cms_app
    home_view = views.HomeView
    project_app = project_app


    def get_urls(self):
        urlpatterns = super(DashboardApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^blog', include(self.blog_app.urls)),
            url(r'^cms', include(self.cms_app.urls)),
            url(r'^project', include(self.project_app.urls)),
            url(r'^$', self.home_view.as_view(), name='home'),
        )
        return urlpatterns


application = DashboardApplication()