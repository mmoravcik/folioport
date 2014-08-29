from django_dynamic_fixture import G

from django.test import TestCase, Client

from folioport.apps.cms import models


class CMSModelTests(TestCase):
    def setUp(self):
        self.text_item = G(models.ItemText, text='Content text content text')
        self.image_item = G(models.ItemImage)
        self.container = G(models.Container)

    def test_assign_item_to_container(self):
        self.text_item.assign_to_container(self.container.id, 10)
        self.assertEqual(1, len(self.container.get_item_objects()))

        self.image_item.assign_to_container(self.container.id, 11)
        self.assertEqual(2, len(self.container.get_item_objects()))
        self.assertIn(self.text_item, self.container.get_item_objects())
        self.assertIn(self.image_item, self.container.get_item_objects())

    def test_deleting_item_unassings_from_container(self):
        self.text_item.assign_to_container(self.container.id, 10)
        self.image_item.assign_to_container(self.container.id, 10)
        self.assertEqual(2, len(self.container.get_item_objects()))

        self.text_item.delete()
        self.assertEqual(1, len(self.container.get_item_objects()))
        self.assertEqual(1, len(models.ContainerItems.objects.all()))

    def test_deleting_container_unassigns_items(self):
        self.text_item.assign_to_container(self.container.id, 10)

        self.assertEqual(1, len(self.container.get_item_objects()))
        self.assertEqual(1, len(models.ContainerItems.objects.all()))

        self.container.delete()
        self.assertEqual(0, len(models.ContainerItems.objects.all()))

    def test_container_render(self):
        item1_rendered = self.text_item.render()
        item2_rendered = self.image_item.render()
        self.text_item.assign_to_container(self.container.id, 10)
        self.image_item.assign_to_container(self.container.id, 10)

        self.assertTrue(item1_rendered in self.container.render())
        self.assertTrue(item2_rendered in self.container.render())