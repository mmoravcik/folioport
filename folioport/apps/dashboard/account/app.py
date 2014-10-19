from django.conf.urls import patterns, url

from folioport.base.app import Application
from . import views


class AccountApplication(Application):
    name = 'account'

    edit_view = views.AccountEditView
    redirect_to_edit_view = views.AccountRedirectToEditView

    def get_urls(self):
        urlpatterns = super(AccountApplication, self).get_urls()
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


application = AccountApplication()