from django.core.urlresolvers import reverse
from django.conf import settings
from django.test import TestCase, Client
from django.contrib.auth import get_user_model



class AccountViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('folioport:account:register')

    def test_register_with_incomplete_data(self):
        response = self.client.get(self.register_url)
        self.assertEqual(200, response.status_code)
        # Try to register with no data submitted
        response = self.client.post(self.register_url,
            {})
        self.assertIn('subdomain', response.context_data['form'].errors)
        self.assertIn('email', response.context_data['form'].errors)
        self.assertIn('password1', response.context_data['form'].errors)
        self.assertIn('password2', response.context_data['form'].errors)

        self.assertEqual(get_user_model().objects.all().count(), 0)

    def test_register_with_valid_data(self):
        response = self.client.post(self.register_url,
            {'email':'aa@aa.com', 'subdomain': 'aaaaa', 'password1': 'aaaaa', 'password2': 'aaaaa'})
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].site.domain, 'aaaaa.' + settings.MAIN_DOMAIN)
        return response

    def test_register_with_invalid_data(self):
        response = self.client.post(self.register_url,
            {'email':'aa@aa.com', 'subdomain': 'aa@aaa', 'password1': 'aaaa', 'password2': 'aaaaa'})
        self.assertIn('subdomain', response.context_data['form'].errors)
        self.assertIn('password2', response.context_data['form'].errors)
        self.assertEqual(len(response.context_data['form'].errors), 2)
        self.assertEqual(get_user_model().objects.all().count(), 0)

    def test_register_with_duplicate_data(self):
        self.test_register_with_valid_data()
        response = self.test_register_with_valid_data()
        self.assertIn('email', response.context_data['form'].errors)
        self.assertIn('subdomain', response.context_data['form'].errors)
        self.assertEqual(len(response.context_data['form'].errors), 2)
        self.assertEqual(get_user_model().objects.all().count(), 1)