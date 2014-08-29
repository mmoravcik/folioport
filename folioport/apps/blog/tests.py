from django_dynamic_fixture import G

from django.test import TestCase, Client

from folioport.apps.blog.models import Post
from folioport.apps.cms import models as cms_models


class BlogModelTests(TestCase):
    def test_new_post_will_have_container_assigned(self):
        blog_post = G(Post, container=None)
        self.assertIsInstance(blog_post.container, cms_models.Container)

    def test_post_delete_will_remove_container_and_its_items(self):
        blog_post = G(Post)
        new_container = G(cms_models.Container)
        self.assertEqual(cms_models.Container.objects.all().count(), 2)

        G(cms_models.ContainerItems, container=blog_post.container)
        other_item = G(cms_models.ContainerItems, container=new_container)
        self.assertEqual(cms_models.Item.objects.all().count(), 2)

        blog_post.delete()

        self.assertEqual(cms_models.Container.objects.all().count(), 1)
        self.assertEqual(cms_models.Item.objects.all().count(), 1)
        self.assertEquals(other_item.container, new_container)

    def test_get_absolute_url(self):
        post = G(Post)
        response = Client().get(post.get_absolute_url())
        self.assertEqual(response.context[-1]['object'], post)
        self.assertEqual(response.status_code, 200)




