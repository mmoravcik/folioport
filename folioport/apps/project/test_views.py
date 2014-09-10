from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.conf import settings

from folioport.apps.project.models import Project


class ProjectViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_detail_view_non_active_project(self):
        project = G(Project, site__id=settings.SITE_ID, active=False)
        response = self.client.get(reverse('folioport:project:detail',
                                   kwargs={'project_slug': 'a', 'pk': project.id}))
        self.assertEqual(404, response.status_code)

    def test_detail_view_different_site(self):
        project = G(Project, site__id=999)
        response = self.client.get(reverse('folioport:project:detail',
                                   kwargs={'project_slug': 'a', 'pk': project.id}))
        self.assertEqual(404, response.status_code)

    def test_detail_view_good_page(self):
        prev_project = G(Project, order=1, site__id=settings.SITE_ID)
        project = G(Project, order=2, site__id=settings.SITE_ID)
        next_project = G(Project, order=3, site__id=settings.SITE_ID)
        response = self.client.get(reverse('folioport:project:detail',
                                   kwargs={'project_slug': 'a', 'pk': project.id}))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['object'], project)
        self.assertEqual(response.context['previous_project'], prev_project)
        self.assertEqual(response.context['next_project'], next_project)