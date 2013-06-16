from django.conf.urls import patterns, include

from folioport.apps.project.app import application as project_app
from folioport.apps.base.app import Application
from folioport.views import HomeView


class FolioportApplication(Application):
    name = 'folioport'

    project_app = project_app
    base_app = Application
    home_view = HomeView

    def get_urls(self):
        urlpatterns = super(FolioportApplication, self).get_urls()
        urlpatterns += patterns('',
            (r'projects/', include(self.project_app.urls)),
            (r'^$', self.home_view.as_view()),
        )
        return urlpatterns


application = FolioportApplication()