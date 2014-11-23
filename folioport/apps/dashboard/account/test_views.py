from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client


class DashboardProfileViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = G(get_user_model())
        self.user2 = G(get_user_model())
        self.user2.save()
        self.user.set_password('1')
        self.user.save()
        self.client.login(email=self.user.email, password='1')

    def test_redirect_to_correct_settings(self):
        response = self.client.get(
            reverse('folioport:dashboard:account:redirect-to-edit'))
        self.assertEqual(301, response.status_code)
        response = self.client.get(
            reverse('folioport:dashboard:account:redirect-to-edit'), follow=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user, response.context['object'])

    def test_prevents_other_users_settings(self):
        response = self.client.get(
            reverse('folioport:dashboard:account:edit', kwargs={'pk': self.user2.id}))
        self.assertEqual(404, response.status_code)
