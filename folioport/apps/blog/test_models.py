from datetime import datetime
from django_dynamic_fixture import G

from django.conf import settings
from django.test import TestCase, Client

from folioport.apps.blog.models import Post
from folioport.apps.cms import models as cms_models


class BlogModelTests(TestCase):
    def _create_post(self, site=settings.SITE_ID, **kwargs):
        return G(Post, site__id=site, **kwargs)

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

    def test_active_posts(self):
        active_post = G(Post, site__id=settings.SITE_ID, active=True)
        nonactive_post = G(Post, site__id=settings.SITE_ID, active=False)
        active_post_different_site = G(Post, site__id=999, active=True)
        self.assertIn(active_post, Post.objects.active().all())
        self.assertEqual(1, len(Post.objects.active().all()))

    def test_previous_next(self):
        posts = [
            self._create_post(title="3", release_date=datetime(2014, 9, 20)), #post[0]
            self._create_post(title="4", release_date=datetime(2014, 10, 20, 1)), #post[1]
            self._create_post(title="5", release_date=datetime(2014, 10, 20, 2)), #post[2]
            self._create_post(title="1", release_date=datetime(2014, 5, 20)), #post[3]
            self._create_post(title="2", release_date=datetime(2014, 6, 20)), #post[4]
        ]

        self.assertEqual(posts[0].next(), posts[1])
        self.assertEqual(posts[0].previous(), posts[4])
        self.assertEqual(posts[1].previous(), posts[0])
        self.assertEqual(posts[1].next(), posts[2])
        self.assertEqual(posts[2].next(), posts[3])
        self.assertEqual(posts[2].previous(), posts[1])
        self.assertEqual(posts[3].previous(), posts[2])

    def test_slug_is_generated(self):
        post = G(Post, title='Test', slug='')
        self.assertEqual(post.slug, 'test')