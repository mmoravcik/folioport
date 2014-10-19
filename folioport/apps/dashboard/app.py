from django.conf.urls import patterns, url, include

from folioport.base.app import Application
from folioport.apps.dashboard.blog.app import application as blog_app
from folioport.apps.dashboard.cms.app import application as cms_app
from folioport.apps.dashboard.project.app import application as project_app
from folioport.apps.dashboard.page.app import application as page_app
from folioport.apps.dashboard.my_css.app import application as my_css_app
from folioport.apps.account.app import application as account_app
from folioport.apps.dashboard.category.app import application as category_app
from folioport.apps.dashboard.account.app import application as account_app

from . import views


class DashboardApplication(Application):
    name = 'dashboard'
    blog_app = blog_app
    cms_app = cms_app
    home_view = views.HomeView
    project_app = project_app
    page_app = page_app
    account_app = account_app
    my_css_app = my_css_app
    category_app = category_app
    account_app = account_app

    def get_urls(self):
        urlpatterns = super(DashboardApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^blog', include(self.blog_app.urls)),
            url(r'^cms', include(self.cms_app.urls)),
            url(r'^project', include(self.project_app.urls)),
            url(r'^page', include(self.page_app.urls)),
            url(r'^css', include(self.my_css_app.urls)),
            url(r'^category', include(self.category_app.urls)),
            url(r'^account', include(self.account_app.urls)),
            url(r'^$', self.home_view.as_view(), name='home'),
        )
        return urlpatterns


application = DashboardApplication()
