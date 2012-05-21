from django.conf.urls.defaults import *

from folioport.base.app import Application
from folioport.project.views import ProjectView, CategoryView
                                  
class ProjectApplication(Application):
    name = 'project'
    project_view = ProjectView
    category_view = CategoryView
        
    def get_urls(self):
        urlpatterns = super(ProjectApplication, self).get_urls()
        urlpatterns += patterns('',
            (r'^(?P<product_slug>[\w-]*)-(?P<pk>\d+)/$', self.project_view.as_view()),
            url(r'^(?P<category_slug>[\w-]*)/$', self.category_view.as_view(), name="category"),

            
        )
        return urlpatterns

application = ProjectApplication()