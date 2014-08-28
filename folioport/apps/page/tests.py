from django_dynamic_fixture import G

from django.test import TestCase

from folioport.apps.page.models import Page
from folioport.apps.cms import models as cms_models


class PageModelTests(TestCase):
    def test_new_post_will_have_container_assigned(self):
        page = G(Page, container=None)
        self.assertIsInstance(page.container, cms_models.Container)

    def test_post_delete_will_remove_container_and_its_items(self):
        page = G(Page)
        new_container = G(cms_models.Container)
        self.assertEqual(cms_models.Container.objects.all().count(), 2)

        G(cms_models.ContainerItems, container=page.container)
        other_item = G(cms_models.ContainerItems, container=new_container)
        self.assertEqual(cms_models.Item.objects.all().count(), 2)

        page.delete()

        self.assertEqual(cms_models.Container.objects.all().count(), 1)
        self.assertEqual(cms_models.Item.objects.all().count(), 1)
        self.assertEquals(other_item.container, new_container)





