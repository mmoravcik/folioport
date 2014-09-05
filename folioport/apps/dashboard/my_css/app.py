from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class MyCssApplication(Application):
    name = 'my_css'

    edit_view = views.MyCssEditView
    redirect_to_edit_view = views.MyCssRedirectToEditView

    def get_urls(self):
        urlpatterns = super(MyCssApplication, self).get_urls()
        urlpatterns += patterns(
            '',
            url(r'/edit/(?P<pk>\d+)/$',
                self.edit_view.as_view(),
                name='edit'),
            url(r'',
                self.redirect_to_edit_view.as_view(),
                name='redirect-to-edit'),
        )
        return urlpatterns


application = MyCssApplication()