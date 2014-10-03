from django_dynamic_fixture import G

from django.test import TestCase, Client
from django.conf import settings

from folioport.apps.page.models import Page
from folioport.apps.cms import models as cms_models


class PageModelTests(TestCase):
    def test_new_page_will_have_container_assigned(self):
        page = G(Page, container=None)
        self.assertIsInstance(page.container, cms_models.Container)

    def test_page_delete_will_remove_container_and_its_items(self):
        page = G(Page)
        new_container = G(cms_models.Container)
        self.assertEqual(cms_models.Container.objects.all().count(), 2)

        G(cms_models.ContainerItems, container=page.container)
        other_item = G(cms_models.ContainerItems, container=new_container)
        self.assertEqual(cms_models.Item.objects.all().count(), 2)

        page.delete()

        self.assertEqual(cms_models.Container.objects.all().count(), 1)
        self.assertEqual(cms_models.Item.objects.all().count(), 1)
        self.assertEqual(other_item.container, new_container)

    def test_get_absolute_url(self):
        page = G(Page, site__id=settings.SITE_ID)
        response = Client().get(page.get_absolute_url())
        self.assertEqual(response.context[-1]['object'], page)
        self.assertEqual(response.status_code, 200)

    def test_can_have_only_one_landing_page(self):
        G(Page, type=Page.LANDING_PAGE, site__id=settings.SITE_ID)
        G(Page, type=Page.CONTENT_PAGE, site__id=settings.SITE_ID)
        G(Page, type=Page.CONTENT_PAGE, site__id=settings.SITE_ID)
        with self.assertRaises(Exception):
            G(Page, type=Page.LANDING_PAGE, site__id=settings.SITE_ID)

    def test_can_save_landing_page(self):
        page = G(Page, type=Page.LANDING_PAGE, site__id=settings.SITE_ID)
        G(Page, type=Page.CONTENT_PAGE, site__id=settings.SITE_ID)
        page.title = 'new'
        page.save()
        self.assertEqual('new', page.title)

    def test_active_projects(self):
        active_page = G(Page, site__id=settings.SITE_ID, active=True)
        nonactive_page = G(Page, site__id=settings.SITE_ID, active=False)
        active_page_different_site = G(Page, site__id=999, active=True)
        self.assertIn(active_page, Page.objects.active().all())
        self.assertEqual(1, len(Page.objects.active().all()))

    def test_slug_is_generated(self):
        project = G(Page, title='Test', slug='')
        self.assertEqual(project.slug, 'test')
