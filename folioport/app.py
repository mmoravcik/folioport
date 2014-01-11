from django.conf.urls import patterns, include

from folioport.apps.project.app import application as project_app
from folioport.apps.blog.app import application as blog_app
from folioport.base.app import Application
from folioport.base.views import HomeView


class FolioportApplication(Application):
    name = 'folioport'

    project_app = project_app
    base_app = Application
    home_view = HomeView
    blog_app = blog_app

    def get_urls(self):
        urlpatterns = super(FolioportApplication, self).get_urls()
        urlpatterns += patterns('',
            (r'projects/', include(self.project_app.urls)),
            (r'blog/', include(self.blog_app.urls)),

            (r'^$', self.home_view.as_view()),
        )
        return urlpatterns


application = FolioportApplication()