from django.conf.urls import patterns, url

from folioport.base.app import Application
from folioport.apps.project.views import ProjectView, CategoryView

from djangoratings.views import AddRatingFromModel


class ProjectApplication(Application):
    name = 'project'
    project_view = ProjectView
    category_view = CategoryView
        
    def get_urls(self):
        urlpatterns = super(ProjectApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^(?P<project_slug>[\w-]*)-(?P<pk>\d+)/$', self.project_view.as_view(), name='project-detail'),
            url(r'^(?P<category_slug>[\w-]*)/$', self.category_view.as_view(), name="category-detail"),
            url(r'^rate/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(), {
                'app_label': 'project',
                'model': 'project',
                'field_name': 'rating',
                }, name='rate_project'),
        )
        return urlpatterns


application = ProjectApplication()