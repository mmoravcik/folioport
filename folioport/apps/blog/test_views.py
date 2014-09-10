from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.conf import settings
from django.test import TestCase, Client

from folioport.apps.blog.models import Post


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


