from django.conf.urls import patterns, url

from folioport.base.app import Application


class BlogApplication(Application):
    name = 'blog'


    def get_urls(self):
        urlpatterns = super(BlogApplication, self).get_urls()
        urlpatterns += patterns('',
            #url(r'', '', name='post-list'),
        )
        return urlpatterns


application = BlogApplication()