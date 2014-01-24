from django.conf.urls import patterns, url, include

from folioport.base.app import Application
from folioport.apps.dashboard.blog.app import application as blog_app
from folioport.apps.dashboard.views import HomeView


class DashboardApplication(Application):
    name = 'dashboard'
    blog_app = blog_app
    home_view = HomeView

    def get_urls(self):
        urlpatterns = super(DashboardApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^blog//', include(self.blog_app.urls)),
            url(r'^$', self.home_view.as_view(), name='home'),
        )
        return urlpatterns


application = DashboardApplication()