from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class BlogApplication(Application):
    name = 'blog'

    list_view = views.PostListView
    edit_view = views.PostEditView
    create_view = views.PostCreateView
    delete_view = views.PostDeleteView

    def get_urls(self):
        urlpatterns = super(BlogApplication, self).get_urls()
        urlpatterns += patterns(
            '',
            url(r'/edit/(?P<pk>\d+)/$',
                self.edit_view.as_view(),
                name='post-edit'),
            url(r'/delete/(?P<pk>\d+)/$',
                self.delete_view.as_view(),
                name='post-delete'),
            url(r'/create',
                self.create_view.as_view(),
                name='post-create'),
            url(r'',
                self.list_view.as_view(),
                name='post-list'),
        )
        return urlpatterns


application = BlogApplication()