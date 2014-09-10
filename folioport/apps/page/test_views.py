from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.conf import settings


from folioport.apps.page.models import Page


class PageViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_detail_view_non_active_page(self):
        page = G(Page, site__id=settings.SITE_ID, active=False)
        response = self.client.get(reverse('folioport:page:detail',
                                   kwargs={'page_slug': 'a', 'pk': page.id}))
        self.assertEqual(404, response.status_code)

    def test_detail_view_different_site(self):
        page = G(Page, site__id=999, active=True)
        response = self.client.get(reverse('folioport:page:detail',
                                   kwargs={'page_slug': 'a', 'pk': page.id}))
        self.assertEqual(404, response.status_code)

    def test_detail_view_good_page(self):
        page = G(Page, site__id=settings.SITE_ID, active=True)
        response = self.client.get(reverse('folioport:page:detail',
                                   kwargs={'page_slug': 'a', 'pk': page.id}))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['object'], page)
