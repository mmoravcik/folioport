from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class CategoryApplication(Application):
    name = 'category'

    list_view = views.CategoryListView
    edit_view = views.CategoryEditView
    create_view = views.CategoryCreateView
    delete_view = views.CategoryDeleteView

    def get_urls(self):
        urlpatterns = super(CategoryApplication, self).get_urls()
        urlpatterns += patterns(
            '',
            url(r'/edit/(?P<app>\w+)/(?P<pk>\d+)/$',
                self.edit_view.as_view(),
                name='edit'),
            url(r'/delete/(?P<app>\w+)/(?P<pk>\d+)/$',
                self.delete_view.as_view(),
                name='delete'),
            url(r'/create/(?P<app>\w+)',
                 self.create_view.as_view(),
                 name='create'),
            url(r'/list/(?P<app>\w+)',
                self.list_view.as_view(),
                name='list'),
        )
        return urlpatterns


application = CategoryApplication()