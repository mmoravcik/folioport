from django.conf.urls import patterns, url

from folioport.base.app import Application
from folioport.apps.project.views import ProjectView, CategoryView


class ProjectApplication(Application):
    name = 'project'
    project_view = ProjectView
    category_view = CategoryView
        
    def get_urls(self):
        urlpatterns = super(ProjectApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^(?P<project_slug>[\w-]*)-(?P<pk>\d+)/$', self.project_view.as_view(), name='project-detail'),
            url(r'^(?P<category_slug>[\w-]*)/$', self.category_view.as_view(), name="category-detail"),
        )
        return urlpatterns


application = ProjectApplication()