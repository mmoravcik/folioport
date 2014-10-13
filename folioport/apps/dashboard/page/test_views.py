from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from folioport.apps.page.models import Page


class DashboardPageViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = G(get_user_model())
        self.user.set_password('1')
        self.user.save()
        self.client.login(email=self.user.email, password='1')

    def test_creation_of_page(self):
        response = self.client.get(reverse('folioport:dashboard:page:create'))
        self.assertEqual(200, response.status_code)

        self.assertEqual(Page.objects.all().count(), 0)

        response = self.client.post(reverse('folioport:dashboard:page:create'), {
            'title': '1',
            'type': Page.LANDING_PAGE,
            }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual(Page.objects.all().count(), 1)
        page = Page.objects.all()[0]
        self.assertEqual(page.user, self.user)
        self.assertEqual(page.site, self.user.site)

