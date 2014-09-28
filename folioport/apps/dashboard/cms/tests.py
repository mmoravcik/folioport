import json

from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.template import Context

from folioport.apps.cms import models


class CMSDashboardViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = G(get_user_model())
        self.user.set_password('1')
        self.user.save()
        self.client.login(email=self.user.email, password='1')
        self.container = G(models.Container, user=self.user)
        self.text_items = [
            G(models.ItemText, text='Content text 1'),
            G(models.ItemText, text='Content text 2'),
            G(models.ItemText, text='Content text 3'),
        ]
        for idx, item in enumerate(self.text_items):
            item.assign_to_container(self.container.id, idx+1)

    def test_item_reorder(self):
        self.assertEqual(self.container.get_item_objects(), [
            self.text_items[0],
            self.text_items[1],
            self.text_items[2],
        ])
        data = {'item_order': ",".join(map(str, [
            models.ContainerItems.objects.get(
                item__item_class=self.text_items[2].__class__.__name__,
                item__item_id=self.text_items[2].id).id,
            models.ContainerItems.objects.get(
                item__item_class=self.text_items[1].__class__.__name__,
                item__item_id=self.text_items[1].id).id,
            models.ContainerItems.objects.get(
                item__item_class=self.text_items[0].__class__.__name__,
                item__item_id=self.text_items[0].id).id,
        ]))}

        self.client.post(
            reverse('folioport:dashboard:cms:items-order-save'), data)

        self.assertEqual(self.container.get_item_objects(), [
            self.text_items[2],
            self.text_items[1],
            self.text_items[0],
        ])

    def test_item_reorder_empty_or_wrong_param(self):
        self.client.post(
            reverse('folioport:dashboard:cms:items-order-save'), {})

        data = {'item_order': [999, 2222, 'ssss']}
        self.client.post(
            reverse('folioport:dashboard:cms:items-order-save'), data)

        self.assertEqual(self.container.get_item_objects(), [
            self.text_items[0],
            self.text_items[1],
            self.text_items[2],
        ])

    def test_container_preview(self):
        response = self.client.get(
            reverse('folioport:dashboard:cms:container-preview',
                    kwargs={'container_id': 0}))
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['status'], 'fail')

        response = self.client.get(
            reverse('folioport:dashboard:cms:container-preview',
                    kwargs={'container_id': self.container.id}))
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['status'], 'success')
        self.assertEqual(json_response['result'], self.container.render(Context({})))
