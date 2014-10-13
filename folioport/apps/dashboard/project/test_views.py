from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from folioport.apps.project.models import Project


class DashboardProjectViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = G(get_user_model())
        self.user.set_password('1')
        self.user.save()
        self.client.login(email=self.user.email, password='1')

    def test_creation_of_project(self):
        response = self.client.get(reverse('folioport:dashboard:project:create'))
        self.assertEqual(200, response.status_code)

        self.assertEqual(Project.objects.all().count(), 0)

        response = self.client.post(reverse('folioport:dashboard:project:create'), {
            'title': '1',
            'thumbnail_width': '1',
            }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual(Project.objects.all().count(), 1)
        project = Project.objects.all()[0]
        self.assertEqual(project.user, self.user)
        self.assertEqual(project.site, self.user.site)

