from django.conf.urls import patterns, url

from folioport.base.app import Application

import views


class AccountApplication(Application):
    name = 'account'
    registration_view = views.UserRegistrationView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'/register/',
                self.registration_view.as_view(),
                name='register'),
            url(r'/login/',
                'django.contrib.auth.views.login',
                {'template_name': 'account/login.html'},
                name='login'),
            url(r'/logout/',
                'django.contrib.auth.views.logout',
                {'next_page': '/'},
                name='logout',
            ),
        )
        return urlpatterns

application = AccountApplication()


