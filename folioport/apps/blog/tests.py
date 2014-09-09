from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.conf import settings
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
        self.assertEqual(other_item.container, new_container)

    def test_get_absolute_url(self):
        post = G(Post, site__id=settings.SITE_ID)
        response = Client().get(post.get_absolute_url())
        self.assertEqual(response.context[-1]['object'], post)
        self.assertEqual(response.status_code, 200)

    def test_active_projects(self):
        active_post = G(Post, site__id=settings.SITE_ID, active=True)
        nonactive_post = G(Post, site__id=settings.SITE_ID, active=False)
        active_post_different_site = G(Post, site__id=999, active=True)
        self.assertIn(active_post, Post.objects.active().all())
        self.assertEqual(1, len(Post.objects.active().all()))


class BlogViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_view(self):
        response = self.client.get(reverse('folioport:blog:post-list'))
        self.assertEqual(200, response.status_code)
        self.assertEquals(list(response.context['object_list']), [])
        G(Post, site__id=settings.SITE_ID, active=True)

        response = self.client.get(reverse('folioport:blog:post-list'))
        self.assertEqual(response.context['object_list'].count(), 1)

        G(Post, site__id=settings.SITE_ID, active=True)
        response = self.client.get(reverse('folioport:blog:post-list'))
        self.assertEqual(response.context['object_list'].count(), 2)

        G(Post, site__id=999, active=True)
        response = self.client.get(reverse('folioport:blog:post-list'))
        self.assertEqual(response.context['object_list'].count(), 2)

        G(Post, site__id=settings.SITE_ID, active=False)
        response = self.client.get(reverse('folioport:blog:post-list'))
        self.assertEqual(response.context['object_list'].count(), 2)

    def test_detail_view_non_active_post(self):
        post = G(Post, site__id=settings.SITE_ID, active=False)
        response = self.client.get(reverse('folioport:blog:post-detail',
                                   kwargs={'post_slug': 'a', 'pk': post.id}))
        self.assertEqual(404, response.status_code)

    def test_detail_view_different_site(self):
        post = G(Post, site__id=999, active=True)
        response = self.client.get(reverse('folioport:blog:post-detail',
                                   kwargs={'post_slug': 'a', 'pk': post.id}))
        self.assertEqual(404, response.status_code)

    def test_detail_view_good_post(self):
        post = G(Post, site__id=settings.SITE_ID, active=True)
        response = self.client.get(reverse('folioport:blog:post-detail',
                                   kwargs={'post_slug': 'a', 'pk': post.id}))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['object'], post)


