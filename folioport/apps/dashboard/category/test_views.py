from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from folioport.apps.project.models import Category


class DashboardCategoryViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = G(get_user_model())
        self.user.set_password('1')
        self.user.save()
        self.client.login(email=self.user.email, password='1')

    def test_creation_of_category(self):
        response = self.client.get(reverse('folioport:dashboard:category:create',
                                           kwargs={'app': 'project'}))
        self.assertEqual(200, response.status_code)

        self.assertEqual(Category.objects.all().count(), 0)
        response = self.client.post(
            reverse('folioport:dashboard:category:create',
                    kwargs={'app': 'project'}), {'name': '1a',}, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual(Category.objects.all().count(), 1)
        cat = Category.objects.all()[0]
        self.assertEqual(cat.user, self.user)
        self.assertEqual(cat.site, self.user.site)

