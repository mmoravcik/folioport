from django_dynamic_fixture import G

from django.test import TestCase, Client

from folioport.apps.project import models
from folioport.apps.cms import models as cms_models


class ProjectModelTests(TestCase):
    def test_previous_next_no_category(self):
        projects = [
            G(models.Project, name="1", order=1),  # project[0]
            G(models.Project, name="3", order=3),  # project[1]
            G(models.Project, name="2", order=2),  # project[2]
            G(models.Project, name="4", order=0)   # project[3]
        ]

        self.assertEqual(projects[0].next(), projects[2])
        self.assertEqual(projects[0].previous(), projects[3])
        self.assertEqual(projects[1].previous(), projects[2])
        self.assertEqual(projects[1].next(), projects[3])
        self.assertEqual(projects[3].previous(), projects[1])

    def test_previous_next_with_category(self):
        categories = [
            G(models.Category, slug='cat1', parent=None),
            G(models.Category, slug='cat2', parent=None)
        ]

        projects = [
            # project[0]
            G(models.Project, name="1", order=1, category=[categories[1]]),
            # project[1]
            G(models.Project, name="3", order=3, category=[categories[1]]),
            # project[2]
            G(models.Project, name="2", order=2, category=[categories[0]]),
            # project[3]
            G(models.Project, name="4", order=0, category=[categories[0]]),
            # project[4]
            G(models.Project, name="5", order=4, category=[categories[0],
                                                           categories[1]]),
            # project[5]
            G(models.Project, name="6", order=5, category=[categories[0]])
        ]

        self.assertEqual(projects[0].next(categories[1].slug), projects[1])
        self.assertEqual(projects[0].previous(categories[1].slug), projects[4])
        self.assertEqual(projects[1].previous(categories[1].slug), projects[0])
        self.assertEqual(projects[1].next(categories[1].slug), projects[4])
        self.assertEqual(projects[3].previous(categories[0].slug), projects[5])
        self.assertEqual(projects[3].next(categories[0].slug), projects[2])

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

    def test_get_absolute_url(self):
        project = G(models.Project)
        response = Client().get(project.get_absolute_url())
        self.assertEqual(response.context[-1]['object'], project)
        self.assertEqual(response.status_code, 200)