from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class ProjectApplication(Application):
    name = 'project'

    list_view = views.ProjectListView
    edit_view = views.ProjectEditView
    create_view = views.ProjectCreateView
    delete_view = views.ProjectDeleteView
    order_save_view = views.ProjectOrderSaveView

    def get_urls(self):
        urlpatterns = super(ProjectApplication, self).get_urls()
        urlpatterns += patterns(
            '',
            url(r'/edit/(?P<pk>\d+)/$',
                self.edit_view.as_view(),
                name='edit'),
            url(r'/delete/(?P<pk>\d+)/$',
                self.delete_view.as_view(),
                name='delete'),
            url(r'/create',
                self.create_view.as_view(),
                name='create'),
            url(r'/order-save',
                self.order_save_view.as_view(),
                name='order-save'),
            url(r'',
                self.list_view.as_view(),
                name='list'),
        )
        return urlpatterns


application = ProjectApplication()