from django.conf.urls import patterns, url

from folioport.base.app import Application
from folioport.apps.blog.views import PostDetailView, PostListView, PostPreview


class BlogApplication(Application):
    name = 'blog'
    post_view = PostDetailView
    list_view = PostListView
    post_preview = PostPreview

    def get_urls(self):
        urlpatterns = super(BlogApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^(?P<post_slug>[\w-]*)-(?P<pk>\d+)/$', self.post_view.as_view(), name='post-detail'),
            url(r'^preview/(?P<post_slug>[\w-]*)-(?P<pk>\d+)/$', self.post_preview.as_view(), name='post-preview'),
            url(r'', self.list_view.as_view(), name='post-list'),
        )
        return urlpatterns


application = BlogApplication()