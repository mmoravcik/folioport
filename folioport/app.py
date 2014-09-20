from django.conf.urls import patterns, include, url

from folioport.apps.project.app import application as project_app
from folioport.apps.blog.app import application as blog_app
from folioport.apps.page.app import application as page_app
from folioport.apps.dashboard.app import application as dashboard_app
from folioport.apps.account.app import application as account_app
from folioport.base.app import Application
from folioport.base import views


class FolioportApplication(Application):
    name = 'folioport'

    project_app = project_app
    base_app = Application
    home_view = views.HomeView
    blog_app = blog_app
    dashboard_app = dashboard_app
    page_app = page_app
    account_app = account_app

    def get_urls(self):
        urlpatterns = super(FolioportApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^accounts', include(self.account_app.urls)),
            (r'^projects/', include(self.project_app.urls)),
            (r'^dashboard/', include(self.dashboard_app.urls)),
            (r'^blog/', include(self.blog_app.urls)),
            (r'^page/', include(self.page_app.urls)),
            url(r'^add/(?P<model_name>\w+)/?$', 'folioport.apps.tekextensions.views.add_new_model'),

            (r'^$', self.home_view.as_view()),
        )
        return urlpatterns


application = FolioportApplication()