from django_dynamic_fixture import G

from django.test import TestCase

from folioport.apps.project import models
from folioport.apps.cms import models as cms_models


class ProjectModelTests(TestCase):
    def test_new_project_will_have_container_assigned(self):
        project = G(models.Project, container=None)
        self.assertIsInstance(project.container, cms_models.Container)

    def test_project_delete_will_remove_container_and_its_items(self):
        project = G(models.Project, container=None)
        new_container = G(cms_models.Container)
        self.assertEqual(cms_models.Container.objects.all().count(), 2)

        G(cms_models.ContainerItems, container=project.container)
        other_item = G(cms_models.ContainerItems, container=new_container)
        self.assertEqual(cms_models.Item.objects.all().count(), 2)

        project.delete()

        self.assertEqual(cms_models.Container.objects.all().count(), 1)
        self.assertEqual(cms_models.Item.objects.all().count(), 1)
        self.assertEquals(other_item.container, new_container)