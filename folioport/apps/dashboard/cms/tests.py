from django_dynamic_fixture import G
from django.core.urlresolvers import reverse

from django.test import TestCase, Client

from folioport.apps.cms import models


class CMSDashboardViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.container = G(models.Container)
        self.container_items = [
            G(models.ContainerItems, container=self.container, position=1),
            G(models.ContainerItems, container=self.container, position=3),
            G(models.ContainerItems, container=self.container, position=2),
        ]

    def test_item_reorder(self):
        self.assertQuerysetEqual(self.container.get_items(), map(repr, [
            self.container_items[0].item,
            self.container_items[2].item,
            self.container_items[1].item,
        ]))

        data = {'item_order': [
            self.container_items[2].id,
            self.container_items[1].id,
            self.container_items[0].id,
        ]}

        self.client.post(
            reverse('folioport:dashboard:cms:items-order-save'), data)

        self.assertQuerysetEqual(self.container.get_items(), map(repr, [
            self.container_items[2].item,
            self.container_items[1].item,
            self.container_items[0].item,
        ]))

    def test_item_reorder_empty_or_wrong_param(self):
        self.client.post(
            reverse('folioport:dashboard:cms:items-order-save'), {})

        data = {'item_order': [999, 2222, 'ssss']}
        self.client.post(
            reverse('folioport:dashboard:cms:items-order-save'), data)

        self.assertQuerysetEqual(self.container.get_items(), map(repr, [
            self.container_items[0].item,
            self.container_items[2].item,
            self.container_items[1].item,
        ]))
